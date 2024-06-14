import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 117.87, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 121.68, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))


  """ ------------ Add more unit tests ------------ """

  def test_getRatio_calculateRatio(self):
    quotes = [
      {'price_a': 119.2, 'price_b': 120.48},
      {'price_a': 117.87, 'price_b': 121.68}
    ]
    for quote in quotes:
      self.assertEqual(getRatio(quote['price_a'], quote['price_b']), (quote['price_a']/quote['price_b']))

  def test_getRatio_calculateRatio_dividebyZero(self):  #for when price_b = 0, making the return value as None
    quotes = [
      {'price_a': 119.2, 'price_b': 0},
      {'price_a': 117.87, 'price_b': 0}
    ]
    for quote in quotes:
      self.assertEqual(getRatio(quote['price_a'], quote['price_b']), None)

  def test_getRatio_calculateRatio_zero(self):      #when price_a = 0, making the return value as 0
    quotes = [
      {'price_a': 0, 'price_b': 120.48},
      {'price_a': 0, 'price_b': 121.68}
    ]
    for quote in quotes:
      self.assertEqual(getRatio(quote['price_a'], quote['price_b']), 0)

if __name__ == '__main__':
    unittest.main()
