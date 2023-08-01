#!/usr/bin/env ruby

# ARGV[0] represents the first command-line argument provided to the script
# In this script, we assume that the first argument is the input data containing TextMe app text message transactions

puts ARGV[0]
  .scan(/(?<=from:|to:|flags:).*?(?=\])/)
    .join(',')
