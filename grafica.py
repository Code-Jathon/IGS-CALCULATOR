def grafica(expre1,expre2,lim1,lim2):
    int(expre1)
    int(expre2)
    int(lim1)
    int(lim2)
    x = np.arange(0,10,0.2)
    y1= np.expre1
    y2=np.expre2
    plt.plot(x,y1,x,y2)  
    plt.fill_between(x, y1,y2, where = [(x > lim1) and (x < lim2) for x in x], color = 'red', alpha = 0.5)      
    plt.grid(True)         
    plt.show()

grafica(expre1, expre2, lim1, lim2)