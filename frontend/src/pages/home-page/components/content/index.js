import React, { Component } from 'react';

import styles from '../../style.css'

export default class Content extends Component {
  render() {
    return (
      <div className={ styles.content_custom }>
        <div className={ 'row ' + styles.box }>
            <div className={ 'col-lg-4 text-center ' + styles.box_inner }>
                <img className="rounded-circle" src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" alt="Generic placeholder image" width="140" height="140"></img>
                <h2>Confiança</h2>
                <p>Donec sed odio dui. Etiam porta sem malesuada magna mollis euismod.</p>
                <p><a className="btn btn-secondary" href="#" role="button">Ver mais &raquo;</a></p>
            </div>
            <div className={ 'col-lg-4 text-center ' + styles.box_inner }>
                <img className="rounded-circle" src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" alt="Generic placeholder image" width="140" height="140"></img>
                <h2>Qualidade</h2>
                <p>Cras mattis consectetur purus sit amet fermentum. Fusce dapibus, tellus ac cursus commodo.</p>
                <p><a className="btn btn-secondary" href="#" role="button">Ver mais &raquo;</a></p>
            </div>
            <div className={ 'col-lg-4 text-center ' + styles.box_inner }>
                <img className="rounded-circle" src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" alt="Generic placeholder image" width="140" height="140"></img>
                <h2>Parceria</h2>
                <p>Vestibulum id ligula porta felis euismod semper. Fusce dapibus.</p>
                <p><a className="btn btn-secondary" href="#" role="button">Ver mais &raquo;</a></p>
            </div>
        </div>
        <hr></hr>
      </div>
    );
  }
}
