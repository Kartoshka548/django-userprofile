#!/usr/bin/python
# -*- coding: utf-8 -*-

class CountRequests(object):
    counter = 0

    def __call__(self):
        self.__class__.counter += 1
        # print self.__class__.counter
        return self.__class__.counter


class Store_sql_Queries_Middleware(object):
    """ Stores all SQL queries to the databases. 
            a) When user is created.
            b) When we want to see some data, filtered or indexed.
            c) When we want to add/remove/update anything related to database
    """

    def process_request(self, request):
        """Request console and log statictics"""

        # Filter any GET request to /favicon.ico is filtered rather than going through all of the routing, logging, and other middlewares that are currently being run.
        if request.path == "/favicon.ico":
            return None

        # initialize and execute request_counter
        request_count = CountRequests()() 
 
        # login/register: username/password verification, can be multiple times but no need to log. stdout is enough.
        if request.method == 'POST':    
            print "Request " + str(request_count) + ": loading " + request.path + " - 'Log-in' or 'register-new' repeating screens (not logging)"        # to console
            return None

        # log journal 
        with open('SQLLOG/log_SQL.txt', 'a+') as logging:
            logging.write("Request %s: %s " % (request_count, request.path))
            if request.user.is_authenticated():
                logging.write("\n")
            else:
                logging.write("(not logged in)\n")

        # logout or page access
        if request.path == "/logout/":    
            print "Request " + str(request_count) + ": loading " + request.path + " - Logging out, redirecting to root"        # to console
        else:
            print "Request " + str(request_count) + ": loading " + request.path         # to console
