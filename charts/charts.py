import matplotlib.pyplot as plt 

def genrate_pie_chart():
    labels=['A','B','C']
    values=[200,34,120]

    fig,ax=plt.subplots()
    ax.pie(values,labels=labels)
    plt.savefig('pie.png')
    plt.close()