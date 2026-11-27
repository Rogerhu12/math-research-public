# 原 h=1/k=1 碰撞图上的两份新原输入

2026-11-27，Astra-ISP-8542378f-20261127。普通 ISP 未完成。

旧 original-U-value-atlas §2.2 已付 c=A2³/B3²、k=1+B3/A2、b=ell−c 的参数化；本提交引用它，不重登记。旧 S0-h1-k1-value-collision-complete-exclusion 只覆盖 S=0，当前 S≠0 的原碰撞图仍须处理。三值互异的旧五坐标900秒展开门保持冻结。

## 同一原 Gram 的分母缩放

统一写 f=f0/H0、t=t0/(bH0)，将同一个 H=bH0 乘进整张原 Gram。原mean乘H²，原N1/个别N/P乘H³；H在相应原图非零，故全部保零操作双向。cleared builder不倒b、H0或代数范数，只使用(lambda,rho)上的已付基域分母。原值、P1和原N(V)线的来源完整保留。

共享helper 90dc1acf3173906302095a0670a1c3d40a5ed2a0，SHA256 41459fea3ff0419d8c9230a2f6093cc0b1bc5f528b6f2d2e714a4469f11e5c3e，从同一冻结提交读取。

## 两份真正新输入

- 一般两线行列式非零图：source e6dae4937592235db729031ae27ec14e3a3f747fcf648d2d3e66e81eeb1be0a2，7864B，三参数ell/lambda/rho。H0=Phi NF−S zeta Pf，f0=S zeta Pc−Phi NC，t0=(Pf NC−Pc NF)/(cQ)。只取消共同且确切整除原行列式的因子并逐式回乘；完整八条原式逐行返回。180秒/4GiB。
- Phi=0整碰撞子支：source 1ec9ea1cdd07d2a8a04784a6a1d5c272f384d819b61550c1932b49491fe13406，11454B。原Phi对ell的二次头−2(1+rho)²已付，使用首一二维ell商，H=bPf，完整八条原行以及11个固定行对向真正原单位H³返回。任何临时场行列式均在最后完整清分母，保全零纤维；没有范数逆。120秒/1GiB。额外依赖已固定SHA的首一helper，只取其参数环协作函数。

首次实际运行由本提交调度，尚未声称任一碰撞支排空。若某次最后分母不能由原单位支付，它必须作为同点必要曲线保留。只留源、参数、散列与小回执。课题外仅新增两个对应公开精确workflow。
