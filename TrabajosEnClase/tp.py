def productos_reponer(stock_total):

    STOCK_MIN=0
    STOCK_ACT=1

    listado_reposicion=[]

    for id_producto, dupla in stock_total.items():

        if dupla[STOCK_ACT]<dupla[STOCK_MIN]:

                cantidad_repo = dupla[STOCK_MIN] - dupla[STOCK_ACT]

                listado_reposicion.append((id_producto,cantidad_repo))

    return listado_reposicion

stock_in ={123:[10,25],
           452:[5,20],
           656:[3,1]
    }

print(type(stock_in))

print(productos_reponer(stock_in))
                                                        
