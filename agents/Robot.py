import agentpy as ap
import numpy as np
from enum import Enum

class Robot(ap.Agent):

   def setup(self):
      self.box_count = 0
      self.fetching = False
      self.target = (0, 0)
      self.delivering = False

   def set_position(self, grid):
      self.grid = grid
      self.position = grid.positions[self]
      
   def get_position(self):
      return self.position
   
   def set_diagonal(self, diagonal):
      self.diagonal = diagonal
      
   def get_vector(self):
      ydelta = self.target[0] - self.position[0]
      xdelta = self.target[1] - self.position[1]
      if xdelta == 0 and ydelta == 0:
         return (0, 0)
      vector = np.array([ydelta, xdelta])
      vector = vector / np.linalg.norm(vector)
      vector = vector.tolist()
      vector[0] = int(round(vector[0]))
      vector[1] = int(round(vector[1]))
      print("Movement vector: " + str(vector))
      return vector
   
   def set_target(self, target: tuple):
      self.target = target
      self.fetching = True
      print("Robot got target at " + str(self.target))
      self.movement_vector = self.get_vector()

   def set_br_router(self, br_router: dict):
      self.br_router = br_router

   def step(self):
      if self.fetching:
         self.movement_vector = self.get_vector()
         self.grid.move_by(self, self.movement_vector)
         self.position = self.grid.positions[self]

   def is_fetching(self):
      return self.fetching

   def is_delivering(self):
      return self.delivering

   def get_target_pos(self):
      return self.target

   def get_counter(self):
      return self.box_count
   def counter_add(self):
      self.box_count += 1
      if (self.box_count == 5):
         self.fetching = False
         self.box_count = 0
   
   def counter_reset(self):
      self.box_count = 0
      self.fetching = True
   
   def set_fetching(self, mode):
      self.fetching = mode