#!/usr/bin/env python
# -- coding: utf-8 --

"""
File:           chatbot.py
Author:         Adeel Ahmad
Email:          adeelahmad84@me.com
Github:         https://github.com/adeelahmad84
Description:    My first chatbot.
"""

import doctest
from chatterbot import ChatBot
import logging
from settings import TWITTER
#import unittest

def main():
    logging.basicConfig(level=logging.INFO)

    chatbot = ChatBot(
        'Adeel',
        #storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
        input_adapter="chatterbot.input.TerminalAdapter",
        output_adapter="chatterbot.output.TerminalAdapter",
        logic_adapters=[
            "chatterbot.logic.MathematicalEvaluation",
            "chatterbot.logic.TimeLogicAdapter",
            "chatterbot.logic.BestMatch"
        ],
        database="./twitter-database.db",
        twitter_consumer_key=TWITTER["CONSUMER_KEY"],
        twitter_consumer_secret=TWITTER["CONSUMER_SECRET"],
        twitter_access_token_key=TWITTER["ACCESS_TOKEN"],
        twitter_access_token_secret=TWITTER["ACCESS_TOKEN_SECRET"],
        trainer="chatterbot.trainers.TwitterTrainer"
    )

    chatbot.train()

    chatbot.logger.info('Trained database generated successfully!')

    while True:
        try:
            bot_input = chatbot.get_response(None)

        except(KeyboardInterrupt, EOFError, SystemExit):
            break

if __name__ == '__main__':
    doctest.testmod()
    main()
