from cspbase import *


def enforce_gac(constraint_list):
    '''Input a list of constraint objects, each representing a constraint, then
		enforce GAC on them pruning values from the variables in the scope of
		these constraints. Return False if a DWO is detected. Otherwise, return True.
		The pruned values will be removed from the variable object cur_domain.
		enforce_gac modifies the variable objects that are in the scope of
		the constraints passed to it.'''

    needsChk = True
    while needsChk: # until done
        needsChk = False # will get set to True if needs another check
        for c in constraint_list: # enforce GAC for each constraint
            for var in c.scope: # enforce GAC for each var in scope
                prune_list = list() # list of values that needs to be pruned
                for val in var.curdom: # each value in var's current domain
                    if (c.has_support(var, val) == False):
                        prune_list.append(val)
                        needsChk = True # needs check since value pruned
                for val in prune_list: # prune the values that did not have support
                    var.prune_value(val)
                if var.cur_domain_size() == 0: # Check for DWO
                    return False
    return True

##############################

def sudoku_enforce_gac_model_1(initial_sudoku_board):
    '''The input board is specified as a list of 9 lists. Each of the
		9 lists represents a row of the board. If a 0 is in the list it
		represents an empty cell. Otherwise if a number between 1--9 is
		in the list then this represents a pre-set board
		position. E.g., the board
		
		-------------------
		| | |2| |9| | |6| |
		| |4| | | |1| | |8|
		| |7| |4|2| | | |3|
		|5| | | | | |3| | |
		| | |1| |6| |5| | |
		| | |3| | | | | |6|
		|1| | | |5|7| |4| |
		|6| | |9| | | |2| |
		| |2| | |8| |1| | |
		-------------------
		would be represented by the list of lists
		
		[[0,0,2,0,9,0,0,6,0],
		[0,4,0,0,0,1,0,0,8],
		[0,7,0,4,2,0,0,0,3],
		[5,0,0,0,0,0,3,0,0],
		[0,0,1,0,6,0,5,0,0],
		[0,0,3,0,0,0,0,0,6],
		[1,0,0,0,5,7,0,4,0],
		[6,0,0,9,0,0,0,2,0],
		[0,2,0,0,8,0,1,0,0]]
		
		
		In model_1 there will be a variable for each cell of the
		board, with domain equal to {1-9} if the board has a 0 at that
		position, and domain equal {i} if the board has a fixed number i
		at that cell.
		
		Model_1 will create BINARY CONSTRAINTS OF NOT-EQUAL between all
		relevant variables (e.g., all pairs of variables in the same
		row), then invoke enforce_gac on those constraints. All of the
		constraints of Model_1 MUST BE binary constraints (i.e.,
		constraints whose scope includes two and only two variables).
		
		This function outputs the GAC consistent domains after
		enforce_gac has been run. The output is a list with the same
		layout as the input list: a list of nine lists each
		representing a row of the board. However, now the numbers in
		the positions of the input list are to be replaced by LISTS
		which are the corresponding cell's pruned domain (current
		domain) AFTER gac has been performed.
		
		For example, if GAC failed to prune any values the output from
		the above input would result in an output would be: (NOTE I HAVE
		PADDED OUT ALL OF THE LISTS WITH BLANKS SO THAT THEY LINE UP IN
		TO COLUMNS. Python would not output this list of list in this
		format. Output will look as if the board values have been replaced
		with lists.)
		
		
        [[[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[                2],[1,2,3,4,5,6,7,8,9],[                9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[                6],[1,2,3,4,5,6,7,8,9]],
         [[1,2,3,4,5,6,7,8,9],[                4],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[                1],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[                8]],
         [[1,2,3,4,5,6,7,8,9],[                7],[1,2,3,4,5,6,7,8,9],[                4],[                2],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[                3]],
         [[                5],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[                3],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]],
         [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[                1],[1,2,3,4,5,6,7,8,9],[                6],[1,2,3,4,5,6,7,8,9],[                5],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]],
         [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[                3],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[                6]],
         [[                1],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[                5],[                7],[1,2,3,4,5,6,7,8,9],[                4],[1,2,3,4,5,6,7,8,9]],
         [[                6],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[                9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[                2],[1,2,3,4,5,6,7,8,9]],
         [[1,2,3,4,5,6,7,8,9],[                2],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[                8],[1,2,3,4,5,6,7,8,9],[                1],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]]
		
		Of course, GAC would prune some variable domains so this would
		not be the outputted list.
		
		'''

    ## generate model
    # create variables for the model
    variables = generate_vars(initial_sudoku_board)
    # create all-diff constraints for the model
    constraints = generate_notEqual_constraints(variables)
    
    ## enforce GAC
    if enforce_gac(constraints):
        # print cells' pruned domains
        print var_curdoms_toString(variables)
    else:
        # DWO case.
        print 'Error enforcing GAC: DWO (domain wipeout) detected'

##############################

def sudoku_enforce_gac_model_2(initial_sudoku_board):
    '''This function takes the same input format (a list of 9 lists
		specifying the board, and generates the same format output as
		sudoku_enforce_gac_model_1.
		
		The variables of model_2 are the same as for model_1: a variable
		for each cell of the board, with domain equal to {1-9} if the
		board has a 0 at that position, and domain equal {i} if the board
		has a fixed number i at that cell.
		
		However, model_2 has different constraints. In particular, instead
		of binary non-equals constraints model_2 has 27 all-different
		constraints: all-different constraints for the variables in each
		of the 9 rows, 9 columns, and 9 sub-squares. Each of these
		constraints is over 9-variables (some of these variables will have
		a single value in their domain). model_2 should create these
		all-different constraints between the relevant variables,
		invoke enforce_gac on those constraints, and then output the list of gac
		consistent variable domains in the same format as for model_1.
		'''
    ## generate model
    # create variables for the model
    variables = generate_vars(initial_sudoku_board)
    # create all-diff constraints for the model
    constraints = generate_allDiff_constraints(variables)
    print 'generated cnsts'
    ## enforce GAC
    if enforce_gac(constraints):
        # print cells' pruned domains
        print var_curdoms_toString(variables)
    else:
        # DWO case.
        print 'Error enforcing GAC: DWO (domain wipeout) detected'

##############################

def sudoku_enforce_gac_model_3(initial_sudoku_board):
    '''This function takes the same input format (a list of 9 lists
        specifying the board, and generates the same format output as
        the other 2 models.
        
        The implementation is a mixture of first 2 models. It enforces 
        first with the not-equals model and does a second level of enforcing
        using all-diff model. This is an attempt to capture the benefits of 
        both of these models to get more pruning in reasonable time and space.
        '''
        
    # create variables for the model
    variables = generate_vars(initial_sudoku_board)
    # create all-diff constraints for the model
    constraints = generate_notEqual_constraints(variables)
    ## enforce GAC
    if enforce_gac(constraints):
        # create all-diff constraints for the model
        constraints = generate_allDiff_constraints(variables)
        ## enforce GAC
        if enforce_gac(constraints):
            # print cells' pruned domains
            print var_curdoms_toString(variables)
        else:
            # DWO case.
            print 'Error enforcing GAC: DWO (domain wipeout) detected'
    else:
        # DWO case.
        print 'Error enforcing GAC: DWO (domain wipeout) detected'

############################## HELPERS ##############################

def generate_vars(sudoku_board):
    ''' Given a sudoku board, creates a matrix of variables.
        
        Naming convention: There is a variable for each position
        on the board. Variable names are set as: 
            'v' + row # + col #
        row and col numbers are of the range: (0...8)
        
        Variable domain: if the value for that position has been
        set then variable domain only contains that value. If it 
        is not set then the domain contains all possible values.
        
        Returns a 9x9 matrix of variables.
        '''
    variables = list()
    for row in range(0,9):
        row_vars = list()
        for col in range(0,9):
            # set domain
            domain = [1,2,3,4,5,6,7,8,9]
            if sudoku_board[row][col] != 0:
                # if a value is already assigned then set the variable
                # domain to contain just that assigned value
                domain = []
                domain.append(sudoku_board[row][col])
            # create and append variable to row
            row_vars.append(Variable('v' + str(row) + str(col), domain))
        # append create row to matrix
        variables.append(row_vars)
    return variables

def generate_notEqual_constraints(variables):
    ''' Generates not-equal constraints for the list of variables.
        'variables' is expected to be a 9x9 matrix of sudoku board variables 
        (as generated from generate_vars() method). 
        
        Returns a list of constraints.
        ''' 
    # list to hold all constraints
    constraints = list()
    
    # generate constraints
    for row in range(0,9):
        for col in range(0,9):
            v = variables[row][col]
            # (scan: go over and create binary not-equal constraints with v)
            # scan down the column
            for i in range(row + 1, 9):
                # create the constraint
                c = Constraint(str(row) + ',' + str(col) + '->'+ str(i) + ',' 
                        + str(col), [variables[row][col], variables[i][col]])
                # generate the satisfying tuples for the constraint
                c.add_satisfying_tuples(generate_sat_tuples
                                    ([variables[row][col], variables[i][col]]))
                # append to the list of constraints
                constraints.append(c)
                
            # scan down the row
            for i in range(col + 1, 9):
                # create the constraint
                c = Constraint(str(row) + ',' + str(col) + '->'+ str(row) + ',' 
                        + str(i), [variables[row][col], variables[row][i]])
                # generate the satisfying tuples for the constraint
                c.add_satisfying_tuples(generate_sat_tuples
                                    ([variables[row][col], variables[row][i]]))
                # append to the list of constraints
                constraints.append(c)
                
            # scan the rest of the subsquare
            for i in range((row/3)*3, (row/3 + 1)*3):
                for j in range((col/3)*3, (col/3 + 1)*3):
                    if (i == row or j == col):
                        continue
                    # create the constraint
                    c = Constraint(str(row) + ',' + str(col) + '->'+ str(i) + ',' 
                            + str(j), [variables[row][col], variables[i][j]])
                    # generate the satisfying tuples for the constraint
                    c.add_satisfying_tuples(generate_sat_tuples
                                        ([variables[row][col], variables[i][j]]))
                    # append to the list of constraints
                    constraints.append(c)
    return constraints

def generate_allDiff_constraints(variables):
    ''' Generates all-diff constraints for the list of variables.
        'variables' is expected to be a 9x9 matrix of sudoku board variables 
        (as generated from generate_vars() method). Creates 3 sets of all-diffs
        : row, column and subblocks of sudoku board. 
        
        Returns a list of constraints.
        '''
    # list to hold all constraints
    constraints = list()
    
    # generate all-diffs for rows
    for i in range(0, 9): # range of rows
        # create the scope
        scope = list()
        for j in range(0, 9):
            scope.append(variables[i][j])
        # create the constraint
        c = Constraint('row_diff_' + str(i), scope)
        # generate the satisfying tuples for the constraint
        c.add_satisfying_tuples(generate_sat_tuples(scope))
        # append to the list of constraints
        constraints.append(c)

    # generate all-diffs for cols
    for i in range(0, 9): # range of cols
        # create the scope
        scope = list()
        for j in range(0, 9):
            scope.append(variables[j][i])
        # create the constraint
        c = Constraint('col_diff_' + str(i), scope)
        # generate the satisfying tuples for the constraint
        c.add_satisfying_tuples(generate_sat_tuples(scope))
        # append to the list of constraints
        constraints.append(c)
        
    # generate all-diffs for subblocks
    for i in range(0, 9): # range of subblocks
        # create the scope
        scope = list()
        for row in range((i/3)*3+0, (i/3)*3+3):
            for col in range((i%3)*3+0, (i%3)*3+3):    
                scope.append(variables[row][col])
        # create the constraint
        c = Constraint('subSqr_diff_' + str(i+1), scope)
        # generate the satisfying tuples for the constraint
        c.add_satisfying_tuples(generate_sat_tuples(scope))
        # append to the list of constraints
        constraints.append(c)
    
    return constraints

def generate_sat_tuples(scope):
    ''' Given variable scope, creates tuples that satisfy all-diff constraints.
        Returns a list of constraints.
        '''
    tuples = list()
    tuples.append([])
    for var in scope:
        new_tuples = list()
        while len(tuples) > 0:
            old_tuple = tuples.pop(0)
            for val in var.cur_domain():
                if val not in old_tuple:
                    tmp = old_tuple[:]
                    tmp.append(val)
                    new_tuples.append(tmp)
        tuples = new_tuples
    return tuples

def var_curdoms_toString(variables):
    ''' Given a matrix of variables (9x9), returns a string that contains 
        the current domain of the variables coverted to string, in the 
        format of the model outputs (as specified on the model functions).
        '''
    string = '['
    for row in range(0,9):
        string = string + '['
        for col in range(0,9):
            v = variables[row][col]
            string = string + str(v.cur_domain()) + ','
        string = string[0:len(string)-1] # delete the last ','
        string = string + '],\n'
    string = string[0:len(string)-2] # delete the last ',\n'
    string = string + ']'
    return string