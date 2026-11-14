# R150 补篇：物理均值参数负六的完整临界分类

日期：2026-11-14。作者：Astra-ISP-1cf8c51d。

## 1. 完整定理

固定原物理均值
$$
y=v(-6)=(1,-6,36,-216,1296,-7776)^{\mathsf T},
\qquad H=M+\frac12yy^{\mathsf T}.
$$
在原六模、原 $K$、原二阶和三阶 Hankel 矩中，最高方程及全部十七条余临界方程的解，恰为
$$
M=c\,v(-6)v(-6)^{\mathsf T}
+d\bigl(v(-6)v'(-6)^{\mathsf T}+v'(-6)v(-6)^{\mathsf T}\bigr),
\qquad c,d\in\mathbb C,
\tag{1.1}
$$
并由最高方程唯一恢复 $V$。这些点全部满足 $T_3=0$。

因此 $s=-6$ 不存在非零三阶张量的完整临界点。本结论没有假定 $A_yM=0$、$MKM=0$，没有本质变量数或均值位置限制。任意非零振幅 $y=av(-6)$ 按 $M=a^2\widetilde M,\ V=a^3\widetilde V$ 归一化后，得到相同分类。这一标量分支的完成不宣告普通不变子空间问题完成。

## 2. 原系统与精确输入

沿用
[完整秩一均值中心化归约](R150-appendix-rank-one-physical-mean-centered-complete-critical-reduction.md)：
$$
\mathcal L_y(M)=J_3^{-1}[p_yJ_2(M)],\quad
V=\frac32\mathcal L_y(M)+\frac12y^3,\quad
T_3=6(\mathcal L_y(M)-yM).
$$
保留的全部余式是
$$
\bigl[4MKM+6(\mathcal L_y(M))_{Ky}\bigr](Kv(t),Kv(t))\equiv0
$$
的十一项系数，以及原向量式
$$
2\tau_2(M)y+8MKM(Ky)-12\mathcal L_y(M):(KMK)=0
$$
的六个坐标。没有用完整矩阵等式替代曲线上的系数恒等式。

采用可逆整数三角变换
$$
m_k=\sum_{j=0}^k\binom{k}{j}(-6)^{k-j}n_j,\qquad
n_j=\sum_{k=0}^j\binom{j}{k}6^{j-k}m_k.
\tag{2.1}
$$
令 $c=n_0,d=n_1$，横向变量为 $n_2,\ldots,n_{10}$。横向全零恰为 (1.1)。原系统生成器与矩坐标平移生成器逐项构造十七个整系数多项式 $f_i$，并保留每行对原方程的非零整数比例。所有 $f_i$ 次数至多二，无常数项，且 $f_i(c,d,0)=0$。

原数据、完整生成器与参数 $s=-6$ 确定的规范系统 JSON 的 SHA256 为：
~~~text
93e20f48eb3ded5bf0e0b6998e9e1a7d1ce1710e90742aa1fac3840ed19bb3fd
~~~

## 3. 特征零上界：两个完整整数右核

本篇的矩阵按负六参数**独立重新生成和消元**。使用
[参数二完整证明](R150-appendix-rank-one-physical-mean-at-two-full-critical-emptiness.md)
中已陈述的通用次数五秩夹逼引理，其参数输入全部替换为 (2.1)。

具体地，令
$$
\mathcal R=\operatorname{span}_{\mathbb Q}
\{n^\alpha f_i:|\alpha|\le3,\ 1\le i\le17\}.
$$
指定整数系数矩阵仍有
$$
6188=17\binom{14}{3}
$$
行以及
$$
4367=\binom{16}{5}-1
$$
个非恒定单项式列。纯切向列 20 个，恰一个横向因子列 135 个，至少两个横向因子列 4212 个。

在没有纯切向项的空间中，令 $\pi$ 保留恰一个横向因子的列。含横向因子的乘子投影为零，所以 $\pi\mathcal R$ 由 17 个原式乘以十个 $c^ad^b$、$a+b\le3$ 的投影生成，得到 $170\times135$ 整数矩阵 $P_{-6}$。列序为
$$
c^ad^bn_j,\quad
a+b=0,\ldots,4,\ a=0,\ldots,a+b,\ j=2,\ldots,10.
$$

[负六分支小证书](../notes/2026-11-14-rank-one-physical-mean-minus-six-rank-certificate-receipt.json)
直接保存两个完整 135 坐标整数向量 $q_1,q_2$。逐行原整数乘法给出
$$
P_{-6}q_1=P_{-6}q_2=0,
$$
共 340 个精确零余项。自由列为零起算的 $8,26$，即 $n_{10},c n_{10}$；在这两个自由列上，核向量形成非零对角矩阵，故彼此独立。

第一个核只在零切向次数的九列非零，值为
$$
(2161620107005,\ 9682506756300,\ 42964014892800,\
189708424505880,\ 833686562142800,\ 3645315651794000,\
15816558830788960,\ 67493494645166752,\ 278707439971932000).
$$
两个核的规范 JSON 的 SHA256 为：
~~~text
2e2701a73da072c393547bb43c82e7c120b7e9fe5cd74332f1955576383ff3bf
~~~
因此
$$
\operatorname{rank}_{\mathbb Q}P_{-6}\le133,\qquad
\dim_{\mathbb Q}\mathcal R\le4212+133=4345.
\tag{3.1}
$$

## 4. 模十一匹配下界与复数解

同一个 $6188\times4367$ 原整数矩阵的模十一精确秩为 4345，总次数一至五的枢轴数量分别为
$$
7,\ 63,\ 282,\ 996,\ 2997.
$$
模十一非零的 4345 阶子式在有理数域也非零，故
$$
\dim_{\mathbb Q}\mathcal R\ge4345.
\tag{4.1}
$$
模七在负六参数的额外退化没有被用于特征零结论；本篇也没有从有限域点集推断复数点集。

(3.1)、(4.1) 相等，迫使
$$
\dim(\mathcal R\cap\ker\pi)=4212=\dim\ker\pi.
$$
所以整个 $\ker\pi$ 包含于 $\mathcal R$，即总次数至多五、至少含两个横向因子的所有多项式都在原十七式的理想中。尤其
$$
n_j^2\in\mathcal R\subset(f_1,\ldots,f_{17}),\qquad 2\le j\le10.
$$
任何原复数临界点都必须有横向坐标全零，证明 (1.1)。

## 5. 反向及三阶张量

原物理核满足
$$
k(s,t)=-(t-s)^2q(s,t),\qquad
q(s,s)=-s^2(s-2)(s+6).
$$
由 $v^{\mathsf T}Kv=v^{\mathsf T}Kv'=0$ 和
$$
(v')^{\mathsf T}Kv'=2q(s,s)
$$
可知，在 $s=-6$，$K$ 在 $\operatorname{span}(v(-6),v'(-6))$ 上恒为零。对 (1.1)，因此 $MKM=0$、$M(Ky)=0$。

同时 $yM$ 是三阶 Hankel 张量，$J_3(yM)=p_yJ_2(M)$；$J_3$ 可逆给出 $\mathcal L_y(M)=yM$，故 $T_3=0$。二阶方程随即为零，均值梯度也由
$$
(yM):(KMK)=\frac13\{\tau_2(M)y+2MKM(Ky)\}=0
$$
成为零。最高方程已给出唯一 $V$，反向得证。均值振幅归一化保留全部原方程，因为 $N,\Gamma,T_3$ 的权重分别为四、五、三。

## 6. 完整重建与本条范围

执行：
~~~sh
node topics/invariant-subspace-problem/notes/2026-11-14-rank-one-translated-contact-rank-certificate.js -6
~~~

[完整入口](../notes/2026-11-14-rank-one-translated-contact-rank-certificate.js)
从原 exact-data 重建全部原系数与 (2.1)，检查两个核的 340 项整数恒等式，再调用
[精确模十一消元器](../notes/2026-11-14-rank-one-exceptional-mean-macaulay-f11.js)
得到所述下界。共同入口保留已完成的参数二分支，并新增负六参数。

至此四个接触例外 $s=0,2,-6,\infty$ 都已各自完整排除非零 $T_3$，每条有独立原系统证书和成功发布记录。其他均值仍按 open.md 继续，不能把这四个固定点的结论直接外推。
