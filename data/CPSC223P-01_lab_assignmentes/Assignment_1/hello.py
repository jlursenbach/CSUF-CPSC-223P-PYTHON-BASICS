'''
Name: Jacobu Ursenbach
Date: 20220824
File Purpose: Multiple Hello Functions
'''

def helloworld() ->str:
  """
  @Name: helloworld
  @Description: returns the string "Hello World
  @Param: None
  @return: "Hello World"
  """
  return "Hello World"

def helloname(name: str) -> None:
  """
  @Name: helloname
  @Description: returns a hello world using custom name
  @Parameters:
  @Return: custom str
  """
  return "Hello " + name + "!"
