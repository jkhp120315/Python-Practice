
import textwrap

def wrap(string, max_width):
  #  word_list = textwrap.fill(string,max_width)
  #  return word_list
    word_list = textwrap.wrap(string,max_width)
    return "\n".join(word_list)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)