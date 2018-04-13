#!/usr/bin/env python3
# coding=utf-8
__author__ = 'cnheider'

from agents.agent import Agent


class PolicyAgent(Agent):
  """
  All policy iteration agents should inherit from this class
  """

  def __init__(self):
    super().__init__()
