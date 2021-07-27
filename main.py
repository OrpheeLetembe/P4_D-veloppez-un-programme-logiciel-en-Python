#! /user/bin/env python3
# coding: utf-8

from controllers.base import Controller
from views.view import View


def main():
	view = View
	game = Controller(view)
	game.run_tournament()


if __name__ == "__main__":
	main()


