#!/usr/bin/env ruby

# Check if the argument matches the regular expression
def match_school(input)
  regex = /School/
  if input.match?(regex)
    puts "The input contains 'School'."
  else
    puts "The input does not contain 'School'."
  end
end

# Get the argument from the command line
if ARGV.empty?
  puts "Please provide an argument."
else
  input_argument = ARGV[0]
  match_school(input_argument)
end
