#!/bin/bash

make run order=1 method=absolute
echo "done order=1 method=absolute"

make run order=1 method=katz
echo "done order=1 method=katz"

make run order=1 method=kneser_ney
echo "done order=1 method=kneser_ney"

make run order=1 method=presmoothed
echo "done order=1 method=presmoothed"

make run order=1 method=unsmoothed
echo "done order=1 method=unsmoothed"

make run order=1 method=witten_bell
echo "done order=1 method=witten_bell"

make run order=2 method=absolute
echo "done order=2 method=absolute"

make run order=2 method=katz
echo "done order=2 method=katz"

make run order=2 method=kneser_ney
echo "done order=2 method=kneser_ney"

make run order=2 method=presmoothed
echo "done order=2 method=presmoothed"

make run order=2 method=unsmoothed
echo "done order=2 method=unsmoothed"

make run order=2 method=witten_bell
echo "done order=2 method=witten_bell"

make run order=3 method=absolute
echo "done order=3 method=absolute"

make run order=3 method=katz
echo "done order=3 method=katz"

make run order=3 method=kneser_ney
echo "done order=3 method=kneser_ney"

make run order=3 method=presmoothed
echo "done order=3 method=presmoothed"

make run order=3 method=unsmoothed
echo "done order=3 method=unsmoothed"

make run order=3 method=witten_bell
echo "done order=3 method=witten_bell"

make run order=4 method=absolute
echo "done order=4 method=absolute"

make run order=4 method=katz
echo "done order=4 method=katz"

make run order=4 method=kneser_ney
echo "done order=4 method=kneser_ney"

make run order=4 method=presmoothed
echo "done order=4 method=presmoothed"

make run order=4 method=unsmoothed
echo "done order=4 method=unsmoothed"

make run order=4 method=witten_bell
echo "done order=4 method=witten_bell"

make run order=5 method=absolute
echo "done order=5 method=absolute"

make run order=5 method=katz
echo "done order=5 method=katz"

make run order=5 method=kneser_ney
echo "done order=5 method=kneser_ney"

make run order=5 method=presmoothed
echo "done order=5 method=presmoothed"

make run order=5 method=unsmoothed
echo "done order=5 method=unsmoothed"

make run order=5 method=witten_bell
echo "done order=5 method=witten_bell"