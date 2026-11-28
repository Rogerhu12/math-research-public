# R1073（续）：相容曲率全迹与固定属二读者

本卷接[§§17–35](R1073-original-first-shell-traces-and-modular-unit-geometry.md)。前卷95284B，按自然证明段续同一编号；保持原固定曲线、点、角色、Tate源和完整精度，不保存可重算数据。主目标未完成。

## 36. 唯一曲率全迹的固定属二迭代微分读者

**已证明。** §35的完整$\mathcal N_p$可用一族预先固定的
属二迭代微分，在原点只读第$p-1$次系数。
这仍保原标记和真实Frobenius，并将普通、惰性写在同一个双覆盖上。

沿(AR1)–(AR2)，取$p$在固定$\mathscr M$中所选位的算术Frobenius
$\gamma$；惰性时允许所有实际$\gamma$，普通时本节仍取
$\mathscr M$完全分裂，故$\gamma=1$。
对每个预先固定的$\gamma\in\operatorname{Gal}(\mathscr M/\mathbf Q)$，
定义特征零微分
$$
 \eta_\gamma=-\sum_{T\in\mathcal T}
       \gamma\!\left(\bar\rho(T)X(T)^2\right)\kappa_T ,
 \qquad
 \kappa_T=\left(X(T)-\frac{y+y(T)}{x-x(T)}\right)\omega .
                                                               \tag{AS1}
$$
记$z=\int_O^P\omega$为物理不变对数，
$\tau(z)=x(P_E(z))^{-1/2}\sim z$，并取固定零初值形式积分
$$
 I_1(z)=\int_0^z\tau(w)\,dw,\qquad
 I_3(z)=\int_0^z\tau(w)^3\,dw .
$$
写$\eta_\gamma=f_\gamma(z)\,dz$。则准确有
$$
 \boxed{\quad
 \mathcal N_p=
 \begin{cases}
 c_p\,[z^{p-1}]\,I_1(z)f_\gamma(z)\pmod p,
                         &p=6n-1,\\[2mm]
 a_p(E_1)\,[z^{p-1}]\,I_3(z)f_1(z)\pmod p,
                         &p=6n+1,\ p\text{在}\mathscr M\text{完全分裂}.
 \end{cases}
 \quad}                                                       \tag{AS2}
$$
两行都对原完整数成立；所有被读系数在对应$p$位整。
由于$\gamma$来自一个固定有限群，
右边是预先固定的有限族，而不是在$p$之后任意更换输入。

### 36.1 完整微分的留数与Cartier来源

$\kappa_T$在$T$的留数为$-1$、在$O$的留数为$1$，
所以$\eta_\gamma$在$T$的留数为
$w_{\gamma,T}=\gamma(\bar\rho(T)X(T)^2)$。
其六单位权为$u^3$：
$\bar\rho(uT)X(uT)^2=u^{-3}\bar\rho(T)X(T)^2$，
而$u^3=\pm1$在任何$\gamma$下不变。
因此$\sum_T w_{\gamma,T}=0$，
且原$O$展开的常数、一次项也分别由非平凡单位权消去。
故$\eta_\gamma$在$O$正则，$f_\gamma$至少二阶。

在所选$p$位，真实Frobenius给
$$
 \overline{w_{\gamma,T}}
          =\bar\rho(T)^pX(T)^{2p}.
$$
这正是(AR2)的同点权。没有把$T$换成$\gamma T$后忘记搬运其它因子。

每个$\kappa_T$来自原素于$p$阶挠除子的真实对数微分：
若$T$阶为$m$，则它是相应除子函数的
$\pm m^{-1}d\log$，符号由上述留数决定。
因此绝对Cartier逐条固定$\kappa_T$，并且
$$
             C\eta_\gamma
                    =-\sum_T\bar\rho(T)X(T)^2\kappa_T .        \tag{AS3}
$$
这个完整右边正是原带$X^2$的微分列；
(AS3)不引入新质量，也不将任何一个标记单独置零。
外部系数的$p$次根与原点上的Cartier必须同时保留。

### 36.2 两个真正属二积分

在固定曲线
$$
                        C_1:\ y^2=\lambda^6+1,\qquad x=\lambda^2
$$
上，第二投影仍为$Q=(\lambda^{-2},y/\lambda^3)$。
原支取$\lambda\sim z^{-1}$、$y\sim-z^{-3}$，
所以$Q(O)=(0,-1)$。
两投影的不变微分准确满足
$$
 Q^*\omega_Q=-\lambda^{-1}\omega,\qquad
 Q^*(x_Q\omega_Q)=-\lambda^{-3}\omega .
$$
于是$I_1$、$I_3$分别是从这个真实$\delta$点起算的
负一型、负二型椭圆积分。它们是同一固定双覆盖的实际微分，
不是只为匹配系数而插入的半权形式函数。

令
$$
                 j_p=-yS_{n-1}(x^3)=\lambda^pG_p(Q).
$$
§35已经证明它是底$E_1$上的有理函数。
由真实第二投影逐项求导，
$$
 D j_p=
 \begin{cases}
      -c_p\lambda^p\tau,&p=6n-1,\\
      -a_p(E_1)\lambda^p\tau^3,&p=6n+1 .
 \end{cases}                                                  \tag{AS4}
$$
这里$D(\lambda^p)=0$在特征$p$中准确成立。
$j_p$只在$O$有极，惰性极阶至多$p-2$，
普通极阶至多$p-4$；完整较低主部仍保在$S_{n-1}$中。

### 36.3 足够且无损的整坐标精度

惰性时可用原严格坐标$s$，§85给$\omega=ds$，
物理对数$\ell(s)=s+O(s^{p^2})$。
全部将要使用的次数小于$p$，所以可直接换回同一个物理$z$。

普通时不能声称全盘$\omega=dz$可在模$p$中整化。
只取真实有理局参$u=-x/y$上$z(u)$的次数至$p-1$整截断
$\widetilde z$，便有
$$
       \widetilde z=u+O(u^2),\qquad
              d\widetilde z/\omega=1+O(u^{p-1}).
$$
次数小于$p$的所有积分分母为$p$单位；
形式逆、$\tau$及本节所需$I_3$截断因此都整。
在两种素型中，
$$
                  \lambda^p=\widetilde z^{-p}
                              (1+O(\widetilde z^{6p})),
$$
其中惰性可直接取$\widetilde z=s$。
普通坐标误差乘$j_p$导数（极阶至多$p-3$）后已经正则，
所以不会影响任何负主部。

由(AS4)可见，$j_p$与
$$
          -b_p\,\widetilde z^{-p}I_\nu(\widetilde z),
       \qquad
       (\nu,b_p)=(1,c_p)\ \text{或}\ (3,a_p(E_1))
$$
具有相同的负主部：
两者差的导数正则，差的极阶严格小于$p$，
而特征$p$中导数为零的负主部只能来自$p$的倍数阶。
因此这里没有残留负主部。
这只须$I_\nu$至$p-1$次；
不对含$p$分母的更深形式对数作非法约化。

### 36.4 真实全局留数等于一个系数

由(AR2)及$f_\gamma$的实际留数，
$$
 \mathcal N_p
     =\sum_Tw_{\gamma,T}j_p(T)
     =-\operatorname{Res}_O(j_p\eta_\gamma).
$$
$j_p$没有其它极，原标记全部在完整和中。
代入已付的负主部得到
$$
 \mathcal N_p
      =b_p\,[\widetilde z^{p-1}]
                I_\nu(\widetilde z)f_\gamma(\widetilde z).
$$
$I_1f_\gamma$至少四阶，$I_3f_\gamma$至少六阶，
所以普通处$\omega/d\widetilde z$的$O(u^{p-1})$误差
不会贡献这一系数。
同理，将整截断换回物理$z$不改变次数$p-1$的值。
这严格证明(AS2)。

由§35，(AS2)所给固定有限族的实际对应系数，
在$S$中具有正上对数密度的非零素数。
尚须证明通常全Sha坏时这些**完整迭代微分系数**为零。
(AS3)把来源锁定在原$X^2$微分列，
但普通的整个AS轨道、惰性的全部Tate权及实际积分因子
仍必须通过真实Kummer操作传递；
仅因它是一个低阶系数，不能把它当作已被旧五槽杀掉。
