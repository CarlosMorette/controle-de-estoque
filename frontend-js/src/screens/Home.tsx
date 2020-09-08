import React, { useState, useEffect } from 'react'
import Header from '../components/Header'
import { Product } from '../constants/Interfaces'
import { requestApi } from '../constants/Functions'
import Table from '../components/Table'
import { Modal } from '../components/Modal'

export default function Home() {

    const [products, setProducts] = useState<Product[]>([])
    const [rowSelected, setRowSelected] = useState<Product | null>(null)
    const [staticData, setStaticData] = useState<Product[]>([
        {name: "Ovo", price: "12.40", category: "carnes e ovos", validity: true}
    ])

    const createObjectData = async (array: Product[]) => {
        const newArray: Product | any = []
        await array.map((o) => {
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
        const arrayProducts = await createObjectData(data)
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
                    columns={["Ação", "Nome", "Preço", "Validade", "Categoria"]}
                    data={products}
                    action={true}
                    modal={(e: boolean) => console.log(e)}
                    rowDataSelected={(row: any) => {
                        setRowSelected({
                            name: row[1].innerText,
                            price: row[2].innerText,
                            validity: row[3].innerText,
                            category: row[4].innerText,
                        })
                    }}
                    />
            </div>
        </div>
    )
}