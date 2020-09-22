def visualizeVector3d(v,equal_axis = None, x_axis=[-3,3],y_axis=[-3,3],z_axis=[-3,3],grid=True,read_by="row"):
    '''
    Function to visualize a vector using matplotlib inline
    
    Params:
        - v : A vector or an array of vectors
        - equal_axis : a list of two elements [start, end] which sets the axes length equal for all three axes
            Alternatively:
            - x_axis, y_axis, z_axis : lists of [start,end] for the respective axis
        - grid : *boolean*, if True (default) the axes-grid will be shown
        - read_by: accepts only "row" or "column". If row (default) is chosen, the matrix is read row by row. A vector [1,2,3] has x= 1, y=2, z=3
            if column is chosen, the matrix is read col by col. So a vector [1,2,3] just represents the 3 x-coordinates of 3 vectors.
        
    '''
    import sys 
    # check that the 3D modules are there
    if 'mpl_toolkits.mplot3d' not in sys.modules:
        try:
            from mpl_toolkits.mplot3d import Axes3D
        except: 
            print("You need the to import Axes3D from mpl_toolkits.mplot3d")
    # define figure
    fig = plt.figure()
        
    # define 3d projection
    ax = fig.gca(projection='3d')
    
    # Set axes length
    
    if equal_axis is not None:
        ax.set_xlim3d(equal_axis[0], equal_axis[1])
        ax.set_ylim3d(equal_axis[0], equal_axis[1])
        ax.set_zlim3d(equal_axis[0], equal_axis[1])
    else:
        ax.set_xlim3d(x_axis[0], x_axis[1])
        ax.set_ylim3d(y_axis[0], y_axis[1])
        ax.set_zlim3d(z_axis[0], z_axis[1])
    
    # Grid in the plot
    ax.grid(grid) 
    # Colors for the vectors
    colors = ['#44cc00','#3366cc','#ff9900', '#cc00ff', '#ff3300', '#000066']
    
    # Check for 3dimensionality of the vectors, if not add 0s (all on the same z-plane)        
    if read_by == 'row':        
        try:
            i = 0
            if v.ndim == 1:
                print(f"Vector {i+1} of coordinates: {v[0]}x, {v[1]}y, {v[2]}z")
                ax.quiver(0,0,0,v[0], v[1], v[2], color=colors[i])
                ax.text(v[0], v[1], v[2],s=f"vec{i+1}")
            elif v.ndim == 2:
                while i < v.shape[0]:
                    if v.shape[1] != 3:
                        z = np.zeros([v.ndim,1])
                        v = np.append(v, z,axis=1)
                    print(f"Vector {i+1} of coordinates: {v[i][0]}x, {v[i][1]}y, {v[i][2]}z")
                    ax.quiver(0,0,0,v[i][0], v[i][1], v[i][2],color=colors[i])
                    ax.text(v[i][0], v[i][1], v[i][2],s=f"vec{i+1}")
                    i += 1
        except:
            print("You didn't provide the function with a valid vector or vector collection")
    elif read_by == "column":
        try:
            i = 0
            if v.ndim == 1:
                print(f"Vector {i+1} of coordinates: {v[0]}x, {v[1]}y, {v[2]}z")
                ax.quiver(0,0,0,v[0], v[1], v[2], color=colors[i])
                ax.text(v[0], v[1], v[2],s=f"vec{i+1}")
            elif v.ndim == 2:
                while i < v.shape[1]:
                    if v.shape[0] != 3:
                        z = np.zeros([1,3])
                        v = np.append(v, z,axis=0)

                    print(f"Vector {i+1} of coordinates: {v[0][i]}x, {v[1][i]}y, {v[2][i]}z")
                    ax.quiver(0,0,0,v[0][i], v[1][i], v[2][i],color=colors[i])
                    ax.text(v[0][i], v[1][i], v[2][i],s=f"vec{i+1}")
                    i += 1
        except:
            print("You didn't provide the function with a valid vector or vector collection")
        
    else:
        print("I can only read by row or column")
    
    plt.show()