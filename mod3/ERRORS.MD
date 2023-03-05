# <div style = 'text-align: center'>Ошибки</div>
## <div style = 'text-align: center'>Было ---> Стало</div>
> ### 1. return <span style="color:red">self.yob - now.year</span> ---> return <span style="color:green">now.year - self.yob</span>
> ### 2. self.name = <span style="color:red">self.</span>name ---> self.name = name
> ### 3. self.address <span style="color:red">==</span> address ---> self.address <span style="color:green">=</span> address
> ### 4. return address is None ---> return <span style="color:green">self.</span>address is None
  