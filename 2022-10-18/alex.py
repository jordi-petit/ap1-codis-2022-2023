# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#   perfect_primes.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#   By: alrodri2 <alrodri2@student.42barcelona.com> +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#   Created: 2022/10/14 11:22:21 by alrodri2           #+#    #+#              #
#   Updated: 2022/10/14 11:22:24 by alrodri2          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def sum_digits(n: int) -> int: #Add up all the digits of a number. Precondition: n >= 0
    i = 0

    while (n > 0):
        i += n % 10
        n = n // 10
    return (i)

def is_prime(n) -> bool: #Return if a number is prime or not. Precondition: n >= 0
    a = 2

    while (a*a <= n): #We can check whether a number is prime or not checking only it's divisibility by all the numbers up to sqrt(n)
        if (n % a == 0):
            return (False)
        a += 1
    return (True)

def is_perfect_prime(n: int) -> bool: #Return if a number is a perfect prime or not. Precondition: n >= 0
    if (n < 2):
        return (False)
    else:
        if (n < 10):
           return (is_prime(n)) #If the number has only one digit, check if it's prime or not.
        else:
            if (is_perfect_prime(sum_digits(n))): #Huga Buga python evaluating second condition after first one is false makes this conditional make sense :)
                return (is_prime(n)) #When n > 10, check if sum_digits(n) is a perfect prime and if is_prime(n).

def main() -> int:
    print(is_perfect_prime(2147483647)) #Testing with the max int to test speed.

if __name__ == "__main__":
    main()



"""
RECURSIVITY STACK WORKFLOW

This is a scheme of how the workflow of the recursive function would work. It was useful to debug certain solutions that were not correct.

        977
########################
#                      #            |
#    TRUE              #  5         V
########################
#   TRUE & f(sum(n))   #
#    TRUE              #  23
########################
#   TRUE &  f(sum(n))  #
#     TRUE             #  977
########################


       587899597 
########################
#                      #
#    FALSE             #  4
########################
#    TRUE & f(sum(n))  #
#    FALSE             #  13
########################
#   TRUE & f(sum(n))   #
#    FALSE             #  67
########################
#   TRUE &  f(sum(n))  #
#     FALSE            #  587899597
########################


       20328307 
########################
#                      #
#    TRUE              #  7
########################
#   FALSE & f(sum(n))  #
#    FALSE             #  25
########################
#   TRUE &  f(sum(n))  #
#     FALSE            #  20328307
########################
"""