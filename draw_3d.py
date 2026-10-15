import numpy as np

#Draw prisms 
def draw_prism(ax, f, x, y, dx, dy, color="teal"):

    # Use the function value at the lower-left corner
    height = f(x, y)

    ax.bar3d(
        x, y, 0,       # base position
        dx, dy, height, # base dimensions and height
        color=color,
        alpha=0.85,
        edgecolor="black",
        linewidth=0.5,
        shade=True
    )

#Draw 3d surfaces
def draw_3d_surface(ax, f, x_min, x_max, y_min, y_max, points = None, markers=True):
    # Define the x and y domains
    x = np.linspace(x_min, x_max, 100)
    y = np.linspace(y_min, y_max, 100)

    # Generate a 2D coordinate grid from the 1D arrays
    X, Y = np.meshgrid(x, y)

    Z = f(X, Y) 

    # Plot the surface
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.4, edgecolor='none')

    
    if markers and points: 
        # Calculate and draw height for specific points 
        for px, py in points:
            pz = f(px, py)  

            # Draw a vertical dotted line from Z = 0 to Z = pz
            ax.plot3D([px, px], [py, py], [0, pz], color='black', linestyle=':', linewidth=2)

            # Scatter a red dots for better visibility
            ax.scatter3D(px, py, pz, color='red', s=50)
        
    # Print value ranges
    #print(f"X range: from {X.min()} to {X.max()}")  
    #print(f"Y range: from {Y.min()} to {Y.max()}")  
    #print(f"Z range (Height): from {Z.min()} to {Z.max()}")  

