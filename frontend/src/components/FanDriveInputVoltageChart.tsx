import {
    Bar,
    BarChart,
    CartesianGrid,
    Legend,
    Tooltip,
    XAxis,
    YAxis,
} from 'recharts';
import React, { ReactElement, useMemo, useRef } from 'react';
import _ from 'lodash';
import { ReadResult } from '../shared/types';

type CurrentSessionTime = Pick<ReadResult, 'name'> & {
    'fan=1': number;
    'fan=2': string;
};

type Props = {
    readResult: ReadResult[];
};

export const FanDriveInputVoltageChart = (props: Props): ReactElement => {
    const { readResult } = props;
    const fanDriveInputVoltage = useRef<CurrentSessionTime[]>([]);

    const readResultName = 'fan.drive.input.voltage';

    fanDriveInputVoltage.current = useMemo((): CurrentSessionTime[] => {
        const values = _(readResult)
            .filter(({ name }) => name === readResultName)
            .map(({ tags, value, name }) => ({
                name,
                [tags]: value,
            }))
            .value();

        return [_.reduce(values, _.assign)];
    }, [readResult]);

    return (
        <BarChart width={400} height={400} data={fanDriveInputVoltage.current}>
            <XAxis dataKey="name" />
            <YAxis dataKey="fan=1" />
            <Tooltip />
            <Legend />
            <Bar type="monotone" dataKey="fan=1" fill="#FF0000" />
            <Bar type="monotone" dataKey="fan=2" fill="#0000FF" />
        </BarChart>
    );
};
