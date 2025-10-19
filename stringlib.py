def strlen(s):
    count = 0
    for _ in s:
       count+=1 
    return count

def str_reverse(s):
    new_string = ""
    for i in range(strlen(s), 0, -1):
        new_string +=  s[i-1]
    return new_string

def str_isalpha(s):
    for char in s:
        if(char >= 'a' and char <= 'z') or (char >= 'A'  and char <= 'Z'):
            pass

        else:
            return False

    return True

def str_isdigit(s):
    for char in s:
        if char >= '0' and char <= '9':
            pass
        else:
            return False
    return True

def str_toupper(s):
    new_string = ''
    for char in s:
        if(char >= 'a' and char <= 'z'):
            new_string += chr(ord(char)-32) 
        else:
            new_string += char
    return new_string

def str_tolower(s):
    new_string = ''
    for char in s:
        if(char >= 'A' and char <= 'Z'):
            new_string += chr(ord(char) + 32)
        else:
            new_string += char
    return new_string

def str_count(string, substring):
    count = 0
    sub_len = strlen(substring)
    s_len = strlen(string)
    for i in range(s_len+1 - sub_len):
        if string[i:i+sub_len] == substring:
            count += 1
    return count

def str_find(string, substring):
   sub_len = strlen(substring)
   s_len = strlen(string)
   for i in range(s_len + 1 - sub_len):
        if string[i:i+sub_len] == substring:
            return i
   return -1 

def str_replace(s, old, new):
    sub_len = strlen(old)
    new_string = ""
    i = 0
    s_len = strlen(s)
    while i < s_len:
        if s[i:i+sub_len] == old:
            new_string += new
            i += sub_len
        else:
            new_string += s[i]
            i+=1
            
    return new_string

def str_strip(s):
    new_string = ''
    for char in s:
        if ord(char) == 32:
            pass
        else:
            new_string += char
    return new_string

def str_split(s, delimiter):
    split_array = []
    current_string = ""
    for char in s:
        if(char != delimiter):
            current_string += char

        else:
            split_array.append(current_string)
            current_string = ""

    split_array.append(current_string)
    return split_array

def str_join(arr, join_char):
   combined_string = ""
   for i  in range(len(arr)):
        if(i == 0):
            combined_string += arr[i]
        else:
            combined_string += join_char + arr[i]
   return combined_string
    
def str_equals_ignore_case(str1, str2):
    if(strlen(str1) != strlen(str2)):
        return False

    if str_toupper(str1) != str_toupper(str2):
         return False

    return True
    
def str_is_palindrome(str):
    lastIndex = strlen(str)-1
    i = 0
    while (i < lastIndex):
        if str[i] != str[lastIndex]:
            return False
        i += 1
        lastIndex -= 1

    return True

def str_to_title(str):
    titleString = ""
    stringLength = strlen(str)

    for i in range(stringLength):
        if(str[i] == ' '):
            titleString += ' '
        elif(i == 0):
            if('A' <= str[i] <= 'Z'):
                titleString += str[i]

            else:
                titleString += chr(ord(str[i]) -32)

        elif (str[i-1] == ' '):
            if('A' <= str[i] <= 'Z'):
                titleString += str[i]

            else:
                titleString += chr(ord(str[i]) -32)
        else:
            if ('a' <= str[i] <= 'z'):
                titleString += str[i]

            else:
                titleString += chr(ord(str[i]) +32)

    return titleString

def str_unique_chars(str):
    unique_chars = set()
    char_arr = []

    for char in str:
        if char not in unique_chars:
            unique_chars.add(char)
            char_arr.append(char)

    return char_arr

def str_freq(str):
    freq_map = dict()
    
    for char in str:
        if char in freq_map:
            freq_map[char] += 1
        else:
            freq_map[char] = 1

    return freq_map

def str_compress(str):
    count = 0
    strComp = ''
    strLength = strlen(str)

    for i in range(strLength):
        if i == 0:
            count += 1 
        elif(i < strLength -1):
            if str[i] != str[i-1]:
                strComp += str[i-1]
                strComp += f"{count}"
                count = 1
            else:
                count += 1
        else:
            strComp += str[i]
            count+=1
            strComp += f"{count}"
        
    print(strComp)
    return strComp

def str_expand(str):

    expandStr = ""
    stringLength = strlen(str)

    for i in range(stringLength):
        if str_isdigit(str[i]):
            for _ in range(int(str[i])):
                expandStr += str[i-1]

    return(expandStr)

def is_vowel(char):
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        return True
    return False

def str_remove_vowels(str):
    new_string = ""
    for char in str:
        if is_vowel(char):
            pass

        else:
            new_string += char

    return new_string


def str_is_anagram(s ,t):
    if(len(s) != len(t)):
        return False

    freqMapS = dict() 
    freqMapT = dict() 

    for i in range(len(s)):
        if s[i] in freqMapS:
            freqMapS[s[i]] += 1
        if t[i] in freqMapT:
            freqMapT[t[i]] +=1
        if s[i] not in freqMapS:
            freqMapS[s[i]] = 1
        if t[i] not in freqMapT:
            freqMapT[t[i]] = 1

    print(freqMapS)
    print(freqMapT)
    if freqMapS == freqMapT:
        return True


    return False

        


