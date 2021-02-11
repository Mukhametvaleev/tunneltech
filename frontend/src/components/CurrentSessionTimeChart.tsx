import { Pie, PieChart, Tooltip } from 'recharts';
import React, { ReactElement, useMemo, useRef } from 'react';
import _ from 'lodash';
import { ReadResult } from 'shared/types';

type CurrentSessionTime = Pick<ReadResult, 'name' | 'value'>;

type Props = {
    readResult: ReadResult[];
};

export const CurrentSessionTimeChart = (props: Props): ReactElement => {
    const { readResult } = props;
    const currentSessionTime = useRef<CurrentSessionTime[]>([]);

    const readResultNames = [
        'current.session.time.elapsed',
        'current.session.time.left',
    ];

    currentSessionTime.current = useMemo(() => {
        const value: CurrentSessionTime[] = _(readResult)
            .filter(({ name }) => readResultNames.includes(name))
            .map((readResult) => _.omit(readResult, ['tags']))
            .value();
        return value;
    }, [readResult]);

    return (
        <PieChart width={400} height={180}>
            <Pie
                startAngle={180}
                endAngle={0}
                data={currentSessionTime.current}
                fill="#FF0000"
                label
                paddingAngle={2}
                dataKey="value"
            />
            <Tooltip />
        </PieChart>
    );
};
