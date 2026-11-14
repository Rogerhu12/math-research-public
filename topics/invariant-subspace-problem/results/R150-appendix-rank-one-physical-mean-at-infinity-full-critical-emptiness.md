# R150 补篇：无穷物理均值的完整临界系统只有切向平面，三阶张量恒为零

日期：2026-11-14。作者：Astra-ISP-1cf8c51d。

## 1. 完整结论

在原六模基及原 $K$ 下，固定非零物理均值 $y=v(\infty)=e_5$。写
$$
H=M+\frac12yy^{\mathsf T},\qquad M_{ij}=m_{i+j}.
$$
若原最高方程与余下全部十七条临界方程成立，则
$$
m_0=\cdots=m_8=0,\qquad T_3=0.
$$
反向也成立：完整临界点集合恰为
$$
M=m_9(e_4e_5^{\mathsf T}+e_5e_4^{\mathsf T})
+m_{10}e_5e_5^{\mathsf T},
\qquad m_9,m_{10}\in\mathbb C,
$$
再由最高方程唯一恢复 $V$。任意振幅 $y=ae_5$、$a\ne0$，经 $M=a^2\widetilde M,\ V=a^3\widetilde V$ 归一化后有相同分类。

本篇不预设 $A_yM=0$、$MKM=0$，也不限制 $T_3$ 或 $V$ 的本质变量数、均值是否位于其本质空间。无穷物理均值下不存在非零 $T_3$ 的完整临界点。这一有限分支结论不等于普通不变子空间问题完成。

## 2. 原十七式与精确输入

使用
[原秩一物理均值完整归约](R150-appendix-rank-one-physical-mean-centered-complete-critical-reduction.md)
的恒等式：
$$
\mathcal L_y(M)=J_3^{-1}[p_yJ_2(M)],\quad
V=\frac32\mathcal L_y(M)+\frac12y^3,\quad
T_3=6(\mathcal L_y(M)-yM),
$$
其中 $p=Ky$。全部余式为
$$
N(Kv(z),Kv(z))\equiv0,\qquad
N=4MKM+6(\mathcal L_y(M))_p,
$$
以及
$$
\Gamma=2\tau_2(M)y+8MKMp
-12\mathcal L_y(M):(KMK)=0.
$$
第一式保留十一项多项式系数，第二式保留六个原向量坐标，没有把曲线上恒等式替换为整个矩阵等式。

具体整系数多项式 $f_1,\ldots,f_{17}$ 来自
[原整数系统](../notes/2026-11-14-rank-one-zero-infinity-centered-systems.json)
的 infinity.equations。每行与原方程之间的非零整数比例已逐行保存在该文件，因此保留全部复数解。

取
$$
c=m_9,\quad d=m_{10},\quad z=(m_0,\ldots,m_8).
$$
原整数系数满足 $f_i(c,d,0)=0$，且次数至多二、无常数项。以下重复使用
[物理参数零分支](R150-appendix-rank-one-physical-mean-at-zero-full-critical-emptiness.md)
第 3—5 节的秩夹逼引理，但全部矩阵系数和本篇证书均由 infinity 分支重新生成，没有由零分支的计算外推。

## 3. 小投影的特征零上界

令 $\mathcal R$ 为 $m^\alpha f_i$、$|\alpha|\le3$ 的线性包。其指定生成矩阵为 $6188\times4367$：

$$
6188=17\binom{14}{3},\qquad
4367=\binom{16}{5}-1.
$$

在总次数一至五的单项式中，纯切向列有 20 个，恰好一个横向因子的列有 135 个，至少两个横向因子的列有 4212 个。$\mathcal R$ 的纯切向系数均为零。

投影 $\pi$ 保留恰好一个横向因子的列。它的核有维数 4212。含有横向因子的乘子经投影后为零，因此 $\pi\mathcal R$ 恰由 17 个原式乘以十个 $c^ad^b$、$a+b\le3$ 后投影得到，形成 $170\times135$ 整数矩阵 $P_\infty$。列序为
$$
c^ad^bm_j,\qquad
a+b=0,\ldots,4,\quad a=0,\ldots,a+b,\quad j=0,\ldots,8.
$$

纯整数消元给出七个独立整数右核向量，逐个代入原 $P_\infty$ 的全部 170 行，共 1190 项整数等式全部精确为零。零起算的自由列为
$$
8,\ 26,\ 98,\ 125,\ 132,\ 133,\ 134,
$$
对应
$$
m_8,\quad c m_8,\quad d^4m_8,\quad c^3d m_8,\quad
c^4m_6,\quad c^4m_7,\quad c^4m_8.
$$
各核向量在上述七自由列中仅自己的一个坐标非零，故独立性直接成立。

第一个核向量只在九个零切向次数列非零，其值为
$$
(-667173150,\ 916517025,\ -1165860900,\ 1165860900,\
-65750400,\ -4102287600,\ 10453284000,\
24721136800,\ 740643383296).
$$
完整七核按所附确定性整数脚本重建；规范 JSON 的 SHA256 是
~~~text
a7eacfb2929c88d7b160d71ccf52d6c8a958be6c0a1a0312a82b7f09e8f8334d
~~~
因此
$$
\operatorname{rank}_{\mathbb Q}P_\infty\le128,\qquad
\dim_{\mathbb Q}\mathcal R\le4212+128=4340. \tag{3.1}
$$

## 4. 原大矩阵的模七下界及提升

同一 $6188\times4367$ 原整数矩阵，在 $\mathbb F_7$ 上的精确消元秩为 4340。指定列序下，总次数一、二、三、四、五的枢轴数依次是
$$
3,\ 62,\ 282,\ 996,\ 2997.
$$
模七非零子式也是有理数域上的非零子式，从而
$$
\dim_{\mathbb Q}\mathcal R\ge4340. \tag{4.1}
$$
这里用的是整数矩阵秩的提升；没有用有限域零点数推断复数解。

合并 (3.1)、(4.1) 后，
$$
\dim\mathcal R
=\dim(\mathcal R\cap\ker\pi)+\dim\pi\mathcal R
=4212+128.
$$
由于两项分别不超过 4212、128，必有 $\ker\pi\subset\mathcal R$。特别地，
$$
m_j^2\in\mathcal R\subset(f_1,\ldots,f_{17})
\qquad(0\le j\le8).
$$
任意原复数解均满足 $m_j=0$，$0\le j\le8$。这个结论使用完整十七式的次数五倍式空间，覆盖原先未闭的 $A_yM\ne0$ 情形。

## 5. 切向平面的反向与三阶张量

在第 1 节所述切向平面上，$yM$ 是三阶 Hankel 张量，且
$$
J_3(yM)=p_yJ_2(M).
$$
由 $J_3$ 可逆，$\mathcal L_y(M)=yM$，因此 $T_3=0$。

原矩阵 $K$ 在 $\operatorname{span}(e_4,e_5)$ 上恒为零，同时
$$
p=Ke_5=(-1,-1,0,0,0,0)^{\mathsf T}.
$$
所以 $MKM=0,\ Mp=0,\ y^{\mathsf T}p=0$，即 $N=0$。再用
$$
(yM):(KMK)
=\frac13\bigl(\tau_2(M)y+2MKMp\bigr)=0
$$
得到 $\Gamma=0$，证明反向。

均值振幅 $a\ne0$ 时，$N,\Gamma,T_3$ 在 $M=a^2\widetilde M$ 下分别有权重四、五、三，归一化不丢失解。定理得证。

## 6. 证书重建

统一入口现同时注册 zero 与 infinity 两个已经分别完成的分支：

~~~sh
node topics/invariant-subspace-problem/notes/2026-11-14-rank-one-exceptional-mean-rank-certificate.js infinity
~~~

[完整入口](../notes/2026-11-14-rank-one-exceptional-mean-rank-certificate.js)
使用同目录的
[整数右核生成器](../notes/2026-11-14-rank-one-exceptional-mean-integer-kernel.js)、
[原矩阵投影与精确核代入](../notes/2026-11-14-rank-one-exceptional-mean-normal-projection.js)
及
[模七精确大矩阵程序](../notes/2026-11-14-rank-one-exceptional-mean-macaulay-f7.js)。
[本分支回执](../notes/2026-11-14-rank-one-physical-mean-infinity-rank-certificate-receipt.json)
保存参数、核哈希和秩。大核可从原系数逐项重建；没有把它拆块传送，也不把外部复核设为发布前置关卡。

至此 $s=0,\infty$ 两个物理均值的完整非零三阶分支均为空。其余物理参数继续按 open.md 处理，不从这两个固定点推出未证明的统一结论。
