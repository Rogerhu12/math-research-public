# 原五槽与倒数曲率之间的驯角色障碍

会话Astra-rank2-Sha-0b097461-20261127。**已证明的形式边界，不是原固定M的反例。**
接R1067 §§106、110–113和R1073 §34；用于排除仅由五槽、全部首野方向迹与Cartier规则消去混项的路线。完整主目标仍未完成。

设$p>211$、$p\equiv5\bmod6$、$q=p^2$、$b=q-1$，
在原严格形式盘取$\Delta=\mu_b$、$\chi(u)=u$。
$\tau=x^{-1/2}=s+O(s^7)$是§91固定属二曲线所选无穷支的真实参数；
这里仅需$\tau/s\in1+sk[[s]]$，$k=\mathbf F_q$。
原$G$、$H_0$满足
$$
 G=s^{-p}+cs+O(s^{5p}),\quad
 g=G/c=s+H_0^p,\quad H_0=c^{-1}s^{-1}+O(s^5),\quad c\in\mathbf F_p^\times.
$$
对任意形式微分$\eta$置$\nu_{20}=C(g^2C\eta)$，并取倒数点曲率所用的真实读者
$$
 r=\operatorname{Res}_O\tau^{-(2p+1)}\nu_{20}.
$$
Cartier与留数的半线性连续两次给
$$
 \begin{aligned}
 r^q&=\operatorname{Res}_O
       \tau^{-(2p+1)q}g^{2p}\eta\\
 &=\operatorname{Res}_O\left\{
    (\tau^{-(2p+1)}H_0^2)^q
    +2s^p(\tau^{-(2p+1)}H_0)^q
    +s^{2p}(\tau^{-(2p+1)})^q
                    \right\}\eta.                     \tag{N1}
 \end{aligned}
$$
全部坐标Jacobian已经保留在微分$\eta$中。

置
$$
 m=2p^2+2p-1,\qquad n=mp=(2p+2)q-p,
 \qquad \eta=e_{\chi^{p+2}}\,d\log(1-s^m).
$$
因为$m\equiv2p+1\bmod b$，
$$
 \gcd(m,p-1)=\gcd(3,p-1)=1,\qquad
 \gcd(m,p+1)=1,
$$
故$\gcd(m,b)=1$。在
$d\log(1-s^m)=-m\sum_{j\ge1}s^{mj-1}ds$
中，$\Delta$投影只保留$mj\equiv p+2\bmod b$的项，
其最小正$j$为$p$，后续为$p+b,p+2b,\ldots$。因此
$$
 \eta=-m\,s^{n-1}ds+
       O\bigl(s^{\,n+mb-1}\bigr)ds.
$$
它的系数在$\mathbf F_q$，$C^2\eta=\eta$，而六次单位权为
$p+2\equiv1\bmod6$，与原源的六次权相同。
但是$e_\chi\eta=0$。所以所有形如
$[s^{jb}]\eta/ds$的原$\chi$槽都为零，不仅§106的五个；
任何先作原完整$\Delta$投影再取首野方向迹的形式读者也全零。

(N1)第一项属于$k((s^q))$，其指数都是$q$倍，不能读到$n\not\equiv0\bmod q$。
第三项的极阶至多$(2p+1)q-2p<n$。
中项的准确首项则为
$$
 \frac2c\,s^{-n}.
$$
其余$\eta$项的阶至少$n+mb$，超过三个核中最大的极阶
$(2p+3)q$，因为$mb>q+p$。于是
$$
                     r^q=-2m/c\ne0.                    \tag{N2}
$$

因此完整五槽（甚至整个$\chi$分量）、$C^2$固定和六次权仍不能形式地推出这个倒数读者为零。缺失的核包含$\chi^{p+2}$型；§112的两个外部系数嵌入只给$\chi,\chi^p$，也不能凭名字替换该型。

这里$\eta$依赖$p$，不声称它来自原固定导子标记的Robert源、固定有理函数$M$或满足其真实全局范数关系。因此(N2)不否定原主命题，也不否定用固定极支撑等额外全局输入接通曲率的可能；它只排除没有这项额外输入的形式消项推论。继续方向是证明原固定源所具有的跨驯角色关系，或直接证明§112固定序列的不整除发生于无限多个素数。
