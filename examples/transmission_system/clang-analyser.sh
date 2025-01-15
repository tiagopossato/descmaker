#!/bin/bash

echo "-----------------"
echo "Building output path and compile database"
echo "-----------------"

sh run.sh --build_only

echo ""
echo "-----------------"
echo "Performing static analysis"
echo "-----------------"

for directory in lib src; do
    find "$directory" \( -name "*.c" -o -name "*.h" \) | while read -r filepath; do
        echo "Verifying $filepath"
        clang-tidy "$filepath" \
            -warnings-as-errors=* \
            -p=build/compile_commands.json \
            -- \
            -std=c99
    done
done