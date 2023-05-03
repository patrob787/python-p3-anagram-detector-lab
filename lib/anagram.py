class Anagram:
    
    def __init__(self, word):
        self.word = word

    def match(self, list):
        def split(word):
          return [letter for letter in word]
      
        split_word = split(self.word)
        split_word.sort()

        matches = []
        
        for item in list:
          split_item = split(item)
          split_item.sort()
          
          if split_word == split_item:
            matches.append(item)
        return matches