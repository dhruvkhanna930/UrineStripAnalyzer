import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import ImageUpload from './components/ImageUpload';

// class ErrorBoundary extends Component {
//   constructor(props) {
//     super(props);
//     this.state = { hasError: false };
//   }

//   static getDerivedStateFromError(error) {
//     // Update state so the next render will show the fallback UI.
//     return { hasError: true };
//   }

//   componentDidCatch(error, errorInfo) {
//     // You can also log the error to an error reporting service
//     console.error('Error caught by boundary:', error, errorInfo);
//   }

//   render() {
//     if (this.state.hasError) {
//       // You can render any custom fallback UI
//       return <h1>Something went wrong.</h1>;
//     }

//     return this.props.children; 
//   }
// }


function App() {
  
  return (
    // <ErrorBoundary>
      <ImageUpload />
    // </ErrorBoundary>
  )
}

export default App