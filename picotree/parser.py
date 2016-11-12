# -*- coding: utf-8 -*-

import logging

from .node import Node

def parse_int(s):
    ret = ''
    for i, c in enumerate(s):
        if c.isdigit():
            ret += c
        elif i > 0:
            return (i, int(ret))
        else:
            break
    return (None, None)

def parse_single_char(s, c, ret=None):
    assert type(c) is str
    assert len(c) == 1

    if s[0] == c:
        return (1, c if ret is None else ret)
    return (None, False)

def parse_comma(s):
    return parse_single_char(s, ',')

def parse_open_paren(s):
    return parse_single_char(s, '(')

def parse_close_paren(s):
    return parse_single_char(s, ')')

def parse_colon(s):
    return parse_single_char(s, ':')

def parse_null_node(s):
    return parse_single_char(s, 'X', ret=None)

def parse_child_node(s):
    p_node = parse_node(s)
    p_null = parse_null_node(s)
    if p_node[0]:
        return (p_node[0], p_node[1])
    elif p_null[0]:
        return (p_null[0], None)
    else:
        return (None, None)

def parse_node(s):
    ptr_move = 0

    # get key
    logging.debug('trying to parse key...')
    p_key = parse_int(s)

    if not p_key[0]:
        return (None, None)

    # if there was a key, parse a :
    logging.debug('success!, key was %d' % p_key[1])
    ptr_move += p_key[0]
    s = s[p_key[0]:]

    logging.debug('trying to parse ":"...')
    p_colon = parse_colon(s)

    if not p_colon[0]:
        return (None, None)

    # if there was a :, parse an (
    logging.debug('success!')
    ptr_move += p_colon[0]
    s = s[p_colon[0]:]

    logging.debug('trying to parse "("...')
    p_open_paren = parse_open_paren(s)

    if not p_open_paren[0]:
        return (None, None)

    # if there was (, parse left child
    logging.debug('success!')
    ptr_move += p_open_paren[0]
    s = s[p_open_paren[0]:]

    logging.debug('trying to parse left node (int)...')
    p_left_child = parse_child_node(s)

    if not p_left_child[0]:
        return (None, None)

    # if there was a left child, parse a ,
    logging.debug('success!, left child was %s' % p_left_child[1])
    ptr_move += p_left_child[0]
    s = s[p_left_child[0]:]

    logging.debug('trying to parse ","...')
    p_comma = parse_comma(s)

    if not p_comma[0]:
        return (None, None)

    # if there was a , parse right child
    logging.debug('success!')
    ptr_move += p_comma[0]
    s = s[p_comma[0]:]

    logging.debug('trying to parse right node (int)...')
    p_right_child = parse_child_node(s)

    if not p_right_child[0]:
        return (None, None)

    # if there was a right node key, parse )
    logging.debug('success!, right child was %s' % p_right_child[1])
    ptr_move += p_right_child[0]
    s = s[p_right_child[0]:]
    p_close_paren = parse_close_paren(s)

    if not p_close_paren[0]:
        return (None, None)

    ptr_move += p_close_paren[0]

    return (ptr_move, Node(key=p_key[1], left=p_left_child[1], right=p_right_child[1]))
