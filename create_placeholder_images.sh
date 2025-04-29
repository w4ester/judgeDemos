#!/bin/bash

# Create placeholder images for all judges
JUDGES=(
  "ron-gula"
  "troy-wilkinson"
  "malcolm-harkins"
  "rinki-sethi"
  "damian-chung" 
  "nick-shevelyov"
  "patricia-titus"
  "michael-baker"
  "peter-kilpe"
  "alicia-lynch"
  "meagan-petri"
)

for judge in "${JUDGES[@]}"; do
  echo "Creating placeholder for $judge"
  echo "Placeholder for $judge's photo" > "images/judges/$judge.jpg"
done

echo "All placeholder images created!"