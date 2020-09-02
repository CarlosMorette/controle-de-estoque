import React, { useState } from 'react'
import { TableProps } from '../constants/Interfaces'
import styles from './../css/components/table.module.css'

export default function Table(props: TableProps){

    const [rowSelected, setRowSelected] = useState()

    const createColumns = (props.columns.map((c, i) => <th key={i}>{c}</th>))

    const a = `
    props.callback((e: any) => {
        console.log(e.target.parentElement.children)
        setRowSelected(e.target.parentElement.children)}
    )
    `

    const createBody = (
        props.data.map((d, i) => {
            return (
                <tr key={i} onClick={(e: any) => props.callback(e.target.parentElement.children)}>
                    {Object.values(d).map((a, i) => <td key={i}>{a}</td>)}
                </tr>
            )
        })
    )

    return (
        <table className={styles.table}>
            <thead>
                <tr>{createColumns}</tr>
            </thead>
            <tbody>
                {createBody}
            </tbody>
        </table>
    )
}