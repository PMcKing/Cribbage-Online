import * as React from 'react';
import { MyFavoriteAnimalList } from './MyFavoriteAnimalList';
import { Socket } from './Socket';

export class Content extends React.Component {
        constructor(props) {
            super(props);
            this.state = {
                'data': '',
            };
        }
        componentDidMount() {
            Socket.on('update', (data) => {
                this.setState(data);
            });
        }
    render() {
        return (
        <div>
            <h1> hello from react! </h1>
            <div>
                Data: {this.state.data}
           </div>
        </div>
        );
    }
}
