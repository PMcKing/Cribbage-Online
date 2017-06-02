import * as React from 'react';
import { MyFavoriteAnimalList } from './MyFavoriteAnimalList';
import { Socket } from './Socket';

export class Content extends React.Component {
        constructor(props) {
            super(props);
            this.state = {
                'data': '',
                'p1Hand': '',
                'p2Hand': '',
                
            };
        }
        componentDidMount() {
            Socket.on('update', (data) => {
                this.setState(data);
            });
            Socket.on('hands', (p1Hand) => {
                this.setState(p1Hand);
            });
        }
    render() {
        return (
        <div>
            <h1> hello from react! </h1>
            <div>
                Data: {this.state.data}
            </div>
            <div>
                p1hand: <img src = {this.state.p1Hand} alt="boohoo" className="img-responsive"/>
            </div>
        </div>
        );
    }
}
