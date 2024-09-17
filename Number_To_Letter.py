"""Program to Convert Numbers to Words 
    ***example***
Number :-2150
o/p:-Two Thousand One Hundred Fifty"""

def number_to_words(num):
    if num == 0:
        return "Zero"
    
    def one(num):
        switcher = {
            1: "One", 2: "Two", 3: "Three", 4: "Four",
            5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
        }
        return switcher.get(num, "")
    
    def two_less_20(num):
        switcher = {
            10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen",
            14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen",
            18: "Eighteen", 19: "Nineteen"
        }
        return switcher.get(num, "")
    
    def ten(num):
        switcher = {
            2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty",
            6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"
        }
        return switcher.get(num, "")
    
    def two(num):
        if not num:
            return ""
        elif num < 10:
            return one(num)
        elif num < 20:
            return two_less_20(num)
        else:
            tenner = num // 10
            rest = num - tenner * 10
            return ten(tenner) + ('' if rest == 0 else ' ' + one(rest))
    
    def three(num):
        hundred = num // 100
        rest = num - hundred * 100
        if hundred and rest:
            return one(hundred) + " Hundred " + two(rest)
        elif not hundred and rest:
            return two(rest)
        elif hundred and not rest:
            return one(hundred) + " Hundred"
        else:
            return ""
    
    billion = num // 1_000_000_000
    million = (num // 1_000_000) % 1_000
    thousand = (num // 1_000) % 1_000
    remainder = num % 1_000
    
    result = ""
    
    if billion:
        result += three(billion) + " Billion"
    if million:
        result += (" " if result else "") + three(million) + " Million"
    if thousand:
        result += (" " if result else "") + three(thousand) + " Thousand"
    if remainder:
        result += (" " if result else "") + three(remainder)
    
    return result.strip()

# Example usage
n=int(input('enter the number :'))
print(number_to_words(n))

