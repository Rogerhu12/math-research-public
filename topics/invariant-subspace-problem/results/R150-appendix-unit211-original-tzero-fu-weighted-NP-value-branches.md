# R150 补充：原 t=0、f=u 的完整 weighted N/P 强迫两条值参数分支

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 1. 完整结论

在原 unit211 Gram 的
$$
t=0,\qquad f=u,\qquad P_{02}\ne0
\tag{1}
$$
分支上，同时使用全部原均值、原 $N_0,N_1,P_1$ 及两 singleton 的 weighted N/P 值条件，有
$$
\boxed{(2\lambda-1)w=0,\qquad \lambda(2\ell-1)=0.}
\tag{2}
$$
其中 $w=\lambda-1-T$。本结论不要求 $\Phi=0$ 或 W，不倒 $\lambda$、$2\lambda-1$、$2\ell-1$、$M$ 或二次头。

因此原复点准确落在以下分支的并：

- $\lambda=0,\ T=-1$；
- $\ell=1/2,\ \lambda=1/2$；
- $\ell=1/2,\ \lambda\ne1/2,\ T=\lambda-1$。

这里是原解的必要分支，不将该并集说成原解集。在当前真正 $\Phi=0$、$Q(1-Q)P_fP_{02}bcD\ne0$ 图上，中间分支完整排除：它只能给
$$
(u,Q,\ell,\lambda,T)=(0,8,1/2,1/2,-1/2),\qquad D=0.
\tag{3}
$$
本引理在一般语境保留另外两支；当前非零孤立 mean 主图的 $\lambda\ne0$ 由独立原规范结果支付。

这加入了已冻结的三二次权理想门没有使用的**完整原 weighted N/P**，不是给该门重排行序、增加资源或重跑。

## 2. 同一真实 Gram 与新的完整身份

令 $a=1-\ell$、$\ell=b+c$，六个参数 $b,c,p,q,r,s$ 自由。记
$$
u=bp+cq,\qquad R_0=br+cs,\qquad
A_1=2\ell u-2R_0.
$$
采用原四行
$$
g_0=(0,0,p,q),\quad
g_1=(0,A_1,r,s),\quad
g_B=(p,r,0,0),\quad
g_C=(q,s,0,0).
\tag{4}
$$
按真正 dual 乘法
$$
(x_0,x_1,x_B,x_C)(y_0,y_1,y_B,y_C)
=(x_0y_0,x_0y_1+x_1y_0,x_By_B,x_Cy_C)
$$
及原 $\tau=(a,1,b,c)$ 定义全部量。(4) 精确给 $F_2=2u$，即 $f=u$；没有只取一个特例或 nilpotent 近似。

设
$$
d=DK(\mathbf1)=(u,d_1,X,Y),\quad
V_2=bp^2+cq^2,\quad T_0=V_2-2u^2,
$$
$$
N_W=bN_4(g_B)+cN_4(g_C),\qquad
P_W=bP_2(g_B)+cP_2(g_C),
$$
$$
E_{W,2}=b(2p-u-X)E_B+c(2q-u-Y)E_C.
$$
本次在全部六变量原多项式环中完整返回
$$
\boxed{N_W=A_1T_0-4\ell u^3+2d_1E_0,}
\tag{5}
$$
$$
\boxed{
2P_W=(1-2\ell)\mathcal N_0+3A_1T_0-8\ell u^3
 +2(2\ell u+d_1)E_0+2E_{W,2}.
}
\tag{6}
$$
这里 $\mathcal N_0=N_4(g_0)$。全部系数和原均值乘子都明确给出；不从数值相合推身份。

(5) 可由
$$
N_4(g_B)=(2d_1+A_1)p^2-4d_1pX
$$
及 C 行同式直接相加，再用原
$$
E_0=V_2+2u^2-2(bpX+cqY),\quad
A_1=2(d_1-\ell u)
$$
得到。对 (6)，原
$$
P_2(g_B)=2X^3-6pX^2+3(1+a)p^2X-2ap^3
$$
沿真实二次均值 $E_B$ 的商是 $2p-u-X$。将两行余式按权相加，再使用同一原 $\mathcal N_0$ 与 $E_0$，得到 (6)。此推导保完整原均值来源。

## 3. 原 jet 与完整值条件

同一个自由 $A_1$ 原 Gram 已给完整身份
$$
2\mathcal P_1-3\mathcal N_0+6aP_{02}=-3A_1T_0.
\tag{7}
$$
代入原
$$
\mathcal N_0=2\lambda P_{02},\quad
\mathcal P_1=3wP_{02},\quad w=\lambda-1-T
$$
得到
$$
A_1T_0=2(\ell+T)P_{02}.
\tag{8}
$$
另一原极化 jet 及均值给
$$
(2\lambda-1)w=\lambda(2\ell-1).
\tag{9}
$$
(7)、(9) 不是新均值平方假设；本次六变量源码也返回其消去前完整原差式。

原值矩为
$$
A_2=2\lambda^2-2\lambda+1,\qquad
B_3=4\lambda^3-6\lambda^2+3\lambda-1.
$$
完整 singleton 值条件给
$$
N_W=2\lambda P_{02}(\ell+2T+A_2),\qquad
P_W=P_{02}(\ell+3T+3A_2+B_3).
\tag{10}
$$
在原均值为零时，把 (8)、(10) 代入 (5)、(6)，得到
$$
E_N=P_{02}\{(\ell+T)-\lambda(\ell+2T+A_2)\}-2\ell u^3=0,
$$
$$
E_P=P_{02}\{(1-2\ell)\lambda+2\ell-3A_2-B_3\}-4\ell u^3=0.
\tag{11}
$$
直接合并原值多项式，严格有
$$
2E_N-E_P=2P_{02}(2\lambda-1)(\lambda-1-T)
       =2P_{02}(2\lambda-1)w.
$$
只除原 $P_{02}\ne0$ 得 (2) 第一式，再由 (9) 得第二式。没有把两个只必要的裸行作无来源替换。

## 4. Phi 中的半值半权分支

仅在 $\lambda=\ell=1/2$ 上，(11) 的第二式直接为
$$
-2u^3=0.
$$
对于原复点，故 $u=0$。真正 $\Phi=0$ 给
$$
\ell=1-\frac{2(u-1)(u-2)}Q,
$$
所以 $Q=8$。原 $P_1$、$f=u$ 给准确恢复
$$
T=-\ell-\frac{K}{Q}\lambda-\frac{KA}{2\ell Q^2},
\quad K=Q+4(u-1),\quad A=4(u-1)^2-Q.
$$
代入 $u=0,Q=8,\ell=\lambda=1/2$ 得 $T=-1/2$，从而 $D=\ell A_2-T^2=0$。这仅排除 (1) 的该物理子分支，不宣称整个一般 $\lambda=1/2$ 图已闭。

## 5. 新精确证书

源码：
[2026-11-28-unit211-original-tzero-fu-weighted-NP-identities-8542.js](../notes/2026-11-28-unit211-original-tzero-fu-weighted-NP-identities-8542.js)。

- blob 50203098bb06e6efebd990aba69f0179c9f1c09f；
- SHA256 8d3552c96106fc9abb74c3b9ce873305810e49702d43674fff663d75b7c5520e；
- 4314 字节，自含纯 V8 BigInt；
- 首次实际 7 ms，734 次整数多项式乘法；
- $F_2=2u$、(5)、(6)、自由 $A_1$ 的两个完整 jet 共五条全差式为零。

[小执行回执](../notes/2026-11-28-unit211-original-tzero-fu-weighted-NP-identities-execution-8542.json)记录实际身份。没有重跑旧四头、旧权理想、Gram20 或任何大参数门。该恒等式本身不倒 $\lambda$。当前主图复用原非零孤立 mean 规范；半权 $w=0$ 的完整原返回另行登记。整个 Phi 和普通 ISP 仍未完成。
