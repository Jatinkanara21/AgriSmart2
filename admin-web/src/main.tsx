import React,{useState}from'react';
import{createRoot}from'react-dom/client';
import'./styles.css';
const API=(import.meta.env.VITE_API_URL||'http://localhost:8000/api/v1') as string;
function App(){
 const[token,setToken]=useState(localStorage.getItem('agrismart_admin_token')||''); const[email,setEmail]=useState(''); const[pw,setPw]=useState(''); const[stats,setStats]=useState<any>(null); const[farms,setFarms]=useState<any[]>([]); const[error,setError]=useState('');
 async function login(){setError('');const r=await fetch(API+'/auth/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({email,password:pw})});const d=await r.json();if(!r.ok){setError(d.detail||'Login failed');return;}localStorage.setItem('agrismart_admin_token',d.access_token);setToken(d.access_token);}
 async function load(){const h={Authorization:'Bearer '+token};const r=await fetch(API+'/admin/stats',{headers:h});if(!r.ok){setError(r.status===403?'Admin access required':'Could not load dashboard');return;}setStats(await r.json());const f=await fetch(API+'/admin/farms',{headers:h});if(f.ok)setFarms(await f.json());}
 React.useEffect(()=>{if(token)load()},[token]);
 if(!token)return <main className="container"><section className="hero"><h1>🌱 AgriSmart Admin</h1><p>Secure platform administration.</p><input placeholder="Email" value={email} onChange={e=>setEmail(e.target.value)}/><input placeholder="Password" type="password" value={pw} onChange={e=>setPw(e.target.value)}/><button onClick={login}>Sign in</button>{error&&<p className="error">{error}</p>}</section></main>;
 return <main className="container"><header><span className="logo">🌱 AgriSmart</span><button onClick={()=>{localStorage.removeItem('agrismart_admin_token');setToken('');}}>Logout</button></header><section className="hero"><h1>Control Center</h1><p>Authenticated administrator dashboard.</p>{error&&<p className="error">{error}</p>}</section>{stats&&<section className="grid">{Object.entries(stats).map(([k,v])=><article className="card" key={k}><h2>{String(v)}</h2><p>{k.replaceAll('_',' ')}</p></article>)}</section>}<section className="card"><h2>Recent Farms</h2><table><thead><tr><th>Farm</th><th>Owner</th><th>Location</th><th>Area</th></tr></thead><tbody>{farms.map(f=><tr key={f.id}><td>{f.name}</td><td>{f.owner_name}<br/>{f.owner_email}</td><td>{f.location||'-'}</td><td>{f.area_acres||'-'}</td></tr>)}</tbody></table></section></main>
}
createRoot(document.getElementById('root')!).render(<React.StrictMode><App/></React.StrictMode>);
