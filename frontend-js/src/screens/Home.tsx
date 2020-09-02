import React, { useState, useEffect } from 'react'
import Header from '../components/Header'
import { Product } from '../constants/Interfaces'
import { requestApi } from '../constants/Functions'
import Table from '../components/Table'

export default function Home() {

    const [products, setProducts] = useState<Product[]>([])
    const [rowSelected, setRowSelected] = useState<Product | null>(null)

    const createObjectData = (array: Product[]) => {
        const newArray: Product | any = []
        array.map(o => {
            const { name, price, validity, category } = o
            const newObject = {
                name,
                price,
                validity: String(validity),
                category
            }
            newArray.push(newObject)
        })
    
        return newArray
    }

    const getProducts = async () => {
        const data = await requestApi("GET", "produto")
        const arrayProducts = createObjectData(data)
        setProducts(arrayProducts)
    }


    useEffect(() => {
        getProducts()
    })

    return (
        <div>
            <Header />
            <div>
                <Table
                    columns={["Nome", "Preço", "Validade", "Categoria"]}
                    data={products}
                />
            </div>
        </div>
    )
}