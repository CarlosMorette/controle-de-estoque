import React from 'react'
import { TableProps } from '../constants/Interfaces'
import styles from './../css/components/table.module.css'

export default function Table(props: TableProps){

    const createColumns = (props.columns.map(c => <th>{c}</th>))
    
    const createBody = (
        props.data.map(d => {
            return (
                <tr>
                    {Object.values(d).map(a => <td>{a}</td>)}
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