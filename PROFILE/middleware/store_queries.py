#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import connection
from django.http import HttpResponse

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
    #def process_request(self, request):
    """Request console and log statictics"""

    """    if request.user.is_authenticated() is not True and request.method == 'POST': 
            CountRequests().__class__.counter -= 1 # no dropped requests in logs (modifying static counter backwards)
            print "Request " + str(request_count) + ": loading " + request.path + " - 'Log-in' or 'register-new' repeating screens (not logging)"        # to console
            return response
            """

    # in incoming request, only sql_request_template visible, which does not carry nothing informative about actual db_request made.  
    # django populates only outgoing_response_sql_requests with actual username, and what to display. 
    def process_response(self, request, response):
        """Response console and log statictics"""


        # Filter any GET request to /favicon.ico is filtered rather than going through all of the routing, logging, and other middlewares that are currently being run.
        if request.path == "/favicon.ico":
            response = HttpResponse()['X-Hacker'] = 'If you are seeing this line, please send us your cv to hr@arpaso.com mentioning this header'
            return response

        # initialize and execute request_counter
        request_count = CountRequests()() 


        ########## Console ############ 
        # logout or page access
        if request.path == "/logout/":    
            print "Request " + str(request_count) + ": loading " + request.path + " - Logging out, redirecting to root"        # to console

        # login/register: username/password verification, can be multiple times but no need to log each. stdout is enough.
        # order important - is_authenticated() must be executed first (if opposite, it's not run when method is not POST) to send auth_query!    
        elif (request.path == "/new/" or request.path == "/login/") and (request.user.is_authenticated() is not True and request.method == 'POST'):
            CountRequests().__class__.counter -= 1 # no dropped requests in logs (modifying static counter backwards)
            print "Request " + str(request_count) + ": loading " + request.path + " - 'Log-in' or 'register-new' repeating screens (not logging)"        # to console

        else:
            print "Request " + str(request_count) + ": loading " + request.path         # to Console
        

        total_time = 0 # assignment before reference (below) - the correct way to do it 

        for query_and_execution in [dict_item.items() for dict_item in connection.queries]:
            print "\n" + query_and_execution[1][1]
            print "---Query execution time (in secs): " + query_and_execution[0][1] + "---" 
            total_time += float(dict_item.get('time'))
        
        print "\n\n%s queries run. Total execution time for this page request: %s \n\n" % (len(connection.queries), total_time)


        ########## FILE: log journal ############
        with open('SQLLOG/log_SQL.txt', 'a+') as logging:
            logging.write("Request %s: %s " % (request_count, request.path))
            
            if request.user.is_authenticated():
                logging.write("\n")
            else:
                logging.write("(not logged in)\n")

            # forloop replaced this single line:    logging.write(connection.queries[-1]['sql']+"\n\n")
            for query in connection.queries:
                logging.write(query['sql']+"\n\n")
                

                 

        return response