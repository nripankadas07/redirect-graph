import unittest
from redirect_graph import analyze
class Tests(unittest.TestCase):
 def test_terminal(self):self.assertEqual(analyze([{'from':'/old','to':'/new'}],['/new'])['findings'],0)
 def test_chain(self):
  r=analyze([{'from':'/a','to':'/b'},{'from':'/b','to':'/c'}],['/c']);self.assertEqual(r['routes'][0]['issue'],'long_chain');self.assertEqual(r['routes'][0]['path'],['/a','/b','/c'])
 def test_cycle(self):
  r=analyze([{'from':'/a','to':'/b'},{'from':'/b','to':'/a'}],[]);self.assertEqual(r['routes'][0]['issue'],'cycle')
 def test_missing(self):self.assertEqual(analyze([{'from':'/x','to':'/404'}],[])['routes'][0]['issue'],'missing_terminal')
 def test_duplicates(self):
  with self.assertRaises(ValueError):analyze([{'from':'/a','to':'/b'},{'from':'/a','to':'/c'}],[])
 def test_unsupported(self):
  for x in ['https://example.com','//host/a','/a?x=2','/a*','/../a']:
   with self.assertRaises(ValueError):analyze([{'from':x,'to':'/b'}],[])
 def test_allowed_chain_limit(self):self.assertEqual(analyze([{'from':'/a','to':'/b'},{'from':'/b','to':'/c'}],['/c'],2)['findings'],0)
