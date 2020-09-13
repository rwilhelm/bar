    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(tcp_echo_client(message, loop))
    # loop.close()

    # blocks are configured in config.yaml
    #blocks = config.get('blocks', [])
    # print(args)

    # creates keys in output dictionary to have them properly ordered (creation
    # order seems to be maintained in dicts)


    # lst = list(remove_repeated_padding(remove_null_string(flatten(FOUT.values())))j

    # lst = map(str,
    #          remove_null_string(flatten(list(FOUT.values()))))

    # [str(item) for sublist in FOUT.values() for item in sublist]
    # [item for sublist in list for item in sublist]
    # [leaf for tree in forest for leaf in tree]
    # [3 2 1 3 2]

    # return " ".join([str(item) for [" ".join(sublist) in FOUT.values()] for item in
    #                 sublist])

    #blocks = get_blocks()
    #stage_out = []
    #i = 0
    #this_block_is_static = None
    #last_block_is_static = None

    #for cur, nxt in iterate(FOUT.iteritems()):
    #    stage_out.append(v)
    #    if 'static' in cur:
	#		pass

        #if 'static' in blocks[name]:  # next block
        #    stage_out[-1] = stage_out[-1].strip()

        ## if not 'static' in block:
        ##    if i > 0 and 'static' in blocks[k].keys():
        ##        stage_out[-1] = stage_out[-1].strip()
        ##    if i < len(FOUT) - 1:

        #last_block_is_static = this_block_is_static
        #last_block = {k: v}
        #i += 1













# run -> watch -> output -> fmt -> stage -> stdout -,
#     '--------'                                    |
#        print <------------------------------------`



    #def func(iterable):
    #    while True:
    #        try:
    #            val = next(iter(iterable))
    #            yield(val)
    #        except StopIteration:
    #            break







        #yield from iter(iterable)

        #yield next(iter(iterable))
        #yield next(iter(iterable))
        #yield (a, b)
        #try:
        #except StopIteration:
        #    #print("hello")
        #    return





    #for name in BLOCKS:
    #    stage_out.append(BLOCKS[name])
    #    #b = next(func(BLOCKS))
    #    #print(b)
    #    #print(list(itertools.islice(BLOCKS, 2)))
    #    #print(BLOCKS[i])

    #fout = iter(BLOCKS)




        # have no padding:
        # - static elements




        #if (
        #    not last
        #    #or 'static' in cur and last
        #    #or 'static' in last
        #):
        #    stage_out.append(block)
        #elif (
        #    last
        #    # no padding in front of first element
        #    #i < 1
        #    # do not put padding in front of static blocks
        #    #or 'static' not in cur
        #    # do not put padding after static blocks
        #    #or 'static' not in last
        #    # do not put padding in front of the first element
        #    or not stage_out
        #    # put padding in front of the last element
        #    or i + 1 == len(BLOCKS)
        #):
        #    stage_out.append(' ')
        #    stage_out.append(block)

        #if i - 3 == len(BLOCKS):
        #    stage_out.append(' ')











        #last = cur if not last else None

        #stage_out.append(block)
        #cur_block = blocks[name]
        #elif 'static' not in next_block:
        #    pass
        #else:
        #i += 1

    #stage_out.append(BLOCKS[next(fout)])

    #while True:
    #    try:
    #        a = next(fout)
    #        b = next(fout)
    #        stage_out.append(a)
    #        stage_out.append(b)
    #        #if 'static' in a:
    #        #    pass
    #        #if 'static' in b:
    #        #    pass
    #        #print(a, b)
    #    except StopIteration:
    #        break

    #for cur, nxt in fout:
    #    stage_out.append(next(fout))


        #if 'static' in BLOCKS[cur] or 'static' in BLOCKS[nxt]:
        #    stage_out.append(' ')

    #stage_out.append(BLOCKS[nxt])
    # stage_out = "".join([str(x) for block in BLOCKS.values() for x in block])










# run -> watch -> output -> fmt -> stage -> stdout -,
#     '--------'                                    |
#        print <------------------------------------`


# [leaf for tree in forest for leaf in tree]

# def flatten(lst: list) -> list:
#    return [lst] if not isinstance(lst, list) else [x for x in lst for x in flatten(x)]




# python -m shared.run BLOCK
# run -> print_block -> yield_block -> uniq -> fmt -,
#        print <------------------------------------`




    # lemonbar = await get_lemonbar()

        _, columns = subprocess.check_output(['stty', 'size']).split()

        # rows, columns = os.popen('stty size', 'r').read().split()

            # print("-" * int(columns))
    # print("{} done".format(name))

            # await lemonbar.communicate(bytes(line, 'utf-8'))
            # await asyncio.gather(log_stream(proc.stdout), log_stream(proc.stderr))
            # await lemonbar()
