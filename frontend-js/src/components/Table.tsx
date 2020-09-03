import React, { useState } from 'react'
import { TableProps } from '../constants/Interfaces'
import styles from './../css/components/table.module.css'
import IconPencil from './../images/icons/pencil.png'

export default function Table(props: TableProps) {

    const createColumns = (props.columns.map((c, i) => <th key={i}>{c}</th>))
    const tdAction = <td 
        className={styles.action}
        onClick={() => props.action(true)}    
    >Action</td>

    const createBody = (
        props.data.map((d, i) => {
            return (
                <tr key={i} onClick={(e: any) => props.rowDataSelected(e.target.parentElement.children)}>
                    {props.action ? tdAction : null}
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