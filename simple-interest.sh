#!/bin/bash

echo "Simple Interest Calculator"
echo "--------------------------"

# Input from user
read -p "Enter Principal amount: " principal
read -p "Enter Rate of Interest (% per year): " rate
read -p "Enter Time Period (years): " time

# Calculate Simple Interest
simple_interest=$(echo "scale=2; ($principal * $rate * $time) / 100" | bc)

echo "--------------------------"
echo "Principal : $principal"
echo "Rate      : $rate%"
echo "Time      : $time years"
echo "Simple Interest = $simple_interest"
