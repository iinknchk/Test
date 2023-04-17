# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    classes.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ktunchar <ktunchar@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/21 23:17:03 by ktunchar          #+#    #+#              #
#    Updated: 2023/03/27 23:27:33 by ktunchar         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# This is a implement of every class that came from class diagram
# TODO : Relation

from datetime import datetime
import time
from enum import Enum


################################################################
# --------------------- MANAGEMENT CLASS --------------------- #
################################################################

class Shop:
	def __init__(self):
		self.product_catalog = [] #AGRET ProductCatalog
		self.users = [] #AGGRESION User
		self.promotions = [] # AGGRESTION Promotion

shop = Shop()

class ProductCatalog:
	def __init__ (self, first_create):
		self.last_update = first_create
		self.product_list = []
	def get_product_by_id(self, id):
		for product in self.product_list:
			if (product.id == id):
				return (product)



#########################################################
# ---------------------- PRODUCT ---------------------- #
#########################################################

class	Product:
	def __init__(self, product_id : str, product_name:str, product_price:int, product_description: str, product_detail : str, product_type : list, product_stock : int, product_specify : str):
		self.id =  product_id
		self.name = product_name
		self.price = product_price
		self.description = product_description
		self.detail = product_detail
		self.type = product_type
		self.stock = product_stock
		self.specify = product_specify

	def	get_product_detail(self):
		return ({
			"id" : self.id, 
			"name" : self.name,
			"price" : self.price, 
			"description" : self.description, 
			"detail" : self.detail, 
			"type" : self.type,
			"stock" : self.stock,
			"specify" : self.specify
	})

class	Promotion:
	def	__init__ (self, product:list,date_start, date_end, discount):
		self.date_start = date_start
		self.date_end = date_end
		self.discount = discount
		self.product = product # COMPOSITION Product

class	Item:
	def	__init__ (self, product, quanity):
		self.quanity = quanity
		self.avaiable_promotion = [] # Composition Promotion
		self.product = product




#########################################################
# ----------------------- USER ------------------------ #
#########################################################

class User:
	def __init__ (self, user_id, email, name):
		self.user_id = user_id
		self.email = email
		self.name = name
		self.account = None # Compostion Account ????

class Account:
	def __init__ (self, email, password):
		self.email = email
		self.password = password

class Admin(User):
	def __init__ (self, salary, shop):
		self.salary = salary
		self.shop = shop # Association (manage) Shop

class Customer(User):
	def __init__ (self):
		pass
		# self.shopping_cart = ShoppingCart('SC' + user_id) # Association ShoppingCart 

class Guest(Customer):
	def	__init__ (self):
		pass

class AuthenticationUser(Customer):
	def	__init__ (self, address):
		self.address = address
		self.order = [] # Aggretion Order
		self.favorite = Favorite() #  Association Favorite

#########################################################
# --------------------- User Hold --------------------- #
#########################################################

class	ShoppingCart:
	def __init__ (self, cart_id):
		self.cart_id = cart_id
		self.total_amount = 0
		self.promotion = shop.promotions # Association Promotion (but it accully need to keep ALL Promotion then it's better if we use Shop)
		self.items = [] # Aggretion Item

class	Favorite:
	def	__init__ (self):
		self.products = [] # Aggretion Product



class	Order:
	def __init__ (self, order_id, date_crate, user):
		self.user = user
		self.order_id = order_id
		self.date_crate = date_crate
		self.items = [] # Agrettion Items
		self.ShippingInfo = [] # Agrettion ShippingInfo
		self.payment = None # Asso Payment
	
	def	cal_total(self):
		pass


class	Payment:
	def	__init__ (self, payment_id, amount, status, order):
		self.order = order
		self.payment_id = payment_id
		self.amount = amount
		self.status = status

class	ShippingInfo:
	def	__init__ (self, shipping_id, shipping_status, tracking_number, date_shipping, date_delivered):
		self.shipping_id = shipping_id
		self.shipping_status = shipping_status
		self.tracking_number = tracking_number
		self.date_shipping = date_shipping
		self.date_delivered = date_delivered

# ENUM #

class	ShippingStatus(Enum):
	NONSHIP = 0
	IN_SHIPPING = 1
	DELIVERED = 2

class	OrderStatus(Enum):
	CANCELED = 0
	PENDING = 1
	CONFRIMED = 2

# product = ProductCatalog(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
# print(product.last_update)
# time.sleep(10)
# print(product.last_update)

pc = ProductCatalog("time")

product_1  = Product("1","Jelly Tint", 259, "Magic Lib Tint", "This is detail\nThis lib made by angle that came from heaven\nHave been sell For 10 year",["Lips"], 9 , "#07")
# promo = Promotion(["65010030"],"1/1/2022","31/12/2023", 39)
pc.product_list.append(product_1)
print((pc.get_product_by_id("1")).get_product_detail())
# shop.promotions.append(promo)
# cart = ShoppingCart("sh11111")