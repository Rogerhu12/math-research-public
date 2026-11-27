# R150：整个一般等权 b=c 原 unit211 分支为空

会话：Astra-ISP-8542378f-20261127。日期：2026-11-27。

## 1. 完整结论及适用范围

在原 essential-four、孤立零单点、单位块型 $2+1+1$ 的剩余原方程中，**整个等权 $b=c$ 分支没有解**。这是原 unit211 分支的排除；它不假定一般 LS 的 Delta=0、W=0 或 Q=1-u，也不由此宣布一般不等权、unit1^4 或普通 ISP 完成。

采用已经登记的对称配对坐标

$$
r^2=1-Q,\quad p=1+r,\quad q=1-r,\quad
b=c=m/2,\quad a=1-m,
$$

其中当前原单位为

$$
m(m-1)Q(Q-1)P_{02}\ne0,\qquad
P_{02}=m(m-1)(2m+3Q-4).
$$

被先前 unit211 归约排除的零配对、相等/相反配对、P0零和u=1等边界仍由各自完整定理覆盖，不在这里重新作为未知假设。下面证明涵盖这个等权图剩余的所有复参数。

## 2. 已付边界和全图原六生成元

以下已发表结论是本定理的证明链，不是新的运行门。

| 原部分 | 完整返回 |
|---|---|
| y=1 | [整 y1 分支](R150-appendix-unit211-equal-weights-singleton-mean-y1-exclusion.md) |
| 原均值首项为零 | [整首项零分支](R150-appendix-unit211-equal-weights-original-mean-leading-zero-exclusion.md) |
| y=1/2 | [整半均值分支](R150-appendix-unit211-equal-weights-half-singleton-mean-exclusion.md) |
| y=0 | [整零均值分支](R150-appendix-unit211-equal-weights-zero-singleton-mean-exclusion.md) |
| T0=0，即J=2m+Q-2=0 | [整T0零分支](R150-appendix-unit211-equal-weights-T0-zero-complete-original-exclusion.md) |
| m=1/2 | [整半权线](R150-appendix-unit211-equal-weights-half-weight-complete-exclusion.md) |

故余图可付 J 和2m-1。在独立原 Gram 坐标 $(x,y,t)$ 中，四个原二次的二次头与选定三次 overlap 头分别有已完整乘回的非零子式

$$
\delta_2=-16m^2(m-1)^2J^2,\qquad
\delta_3=\frac{8(m-1)Q(Q-1)^2}{J}.
$$

这两个式子的全部因子都已支付，所以[六生成元定理](R150-appendix-unit211-equal-weights-global-original-six-generator-module.md)覆盖整个余图：

$$
B=(1,x,y,t,y^2,yt).
$$

这不声称 B 自由或正规形唯一。原另外两条 overlap、全部十八条真乘法，以及原NS/PS/Dval已由[完整原返回](R150-appendix-unit211-equal-weights-six-generator-original-multiplication-and-value-rows.md)给出，后续每条参数关系都保留原trace。

## 3. 完整权覆盖的所有因子

原十条六列必要行给出完整cofactor曲线 C、D，全部六列实际乘回。其固定49阶QQ结式给[完整824次覆盖](R150-appendix-unit211-equal-weights-complete-824-degree-original-weight-cover.md)。只剥已付单位后，任何余图原解都须满足

$$
(2m+1)F_{236}(m)F_{243}(m)=0.
$$

两个大因子已经各自完整返回原方程：

- [整个F243](R150-appendix-unit211-equal-weights-entire-F243-original-Gauss-exclusion.md)：新同点原NS*x行形成52阶结式，在模1009保度后以完整Bézout1和Gauss引理排所有复根。
- [整个F236](R150-appendix-unit211-equal-weights-entire-F236-original-cofactor-exclusion.md)：另一组原六行形成51阶结式，保旧五行头零，模1009保度Bézout1排所有复根。

这两项都没有倒置未知参数主元，也没有只选择一个复嵌入。因此最后唯一待返回的整权线是 $m=-1/2$。

## 4. 最后整条负半权线的原QQ返回

现在在原 Gram 重建之前固定 $m=-1/2$。这时

$$
P_{02}=\frac34(3Q-5),\qquad T_0=\frac12(Q-3).
$$

所以此线只使用已付单位

$$
Q(Q-1)(3Q-5)(Q-3)\ne0.
$$

其中 Q=3 恰是已经完整排除的 T0零支；没有凭此次Cramer或Bareiss的中间主元将它删去。六生成元首项分别退化为

$$
\delta_2=-9(Q-3)^2,\qquad
\delta_3=-\frac{12Q(Q-1)^2}{Q-3},
$$

仍在整个允许权线上非零。源码从原四维代数重建原mean、N0/P1和加权N/P，重新形成同一原四二次、六条monic规则和十八条乘法；每一步均实际乘回。

仍将非恒数五列放前，取原五行 $(0,1,2,3,5)$。其余五条原行依次为 $(8,4,6,7,9)$。对每条都用原五阶子式形成完整六列cofactor并乘回，只剥上述四个已付原权因子，得到

$$
A_0,A_1,A_2,A_3,A_4\in\mathbb Q[Q],
$$

$$
(\deg A_0,\deg A_1,\deg A_2,\deg A_3,\deg A_4)
=(23,29,29,29,29).
$$

任何当前原解都使这五式为零，包括所选非恒数头的所有零纤维。实际QQ扩展Euclid完整给出

$$
U(Q)A_0(Q)+V(Q)A_2(Q)=1,\qquad
\deg U=28,\quad\deg V=22.
$$

五项Bézout向量的次数是 $(28,-1,22,-1,-1)$，其三项为零；源码把完整五项乘回1，未用模数、近似根或抽样点。因此此整条负半权线没有原解。

这也排除了完整权覆盖最后的因子2m+1，故整个一般等权b=c分支为空。原物理Dval不再需要在这最后余图中另作假设来制造矛盾：已经由必要的原六式获得单位理想；此前使用Dval排除的边界仍由其完整原证明支付。

## 5. 对后续一般不等权图的准确影响

在对称权坐标中

$$
b-c=\frac{u-\ell}{r}.
$$

原 $r\ne0$，故一般剩余图现在可以支付 $\ell-u\ne0$。这只使用本定理排除的等权面，不支付 $\ell$、T 或任何其他未闭系数。

特别在已登记的一般 LS/W=0 权图，

$$
e=u-1,\quad Q=ek,\quad V=(e+1)k+2,\qquad
\ell=\frac{u((k+2)^2-2ek)}{kV},
$$

直接恒等整理为

$$
\ell-u=\frac{u(k+2)(2-Q)}{kV}.
$$

既有u、k、V为单位，因此在该余图上可进一步支付k+2和Q-2。J19、C9及整个一般W有限支仍须独立处理，不因上述恒等式自动排空。

## 6. 最后新输入的实际身份

自含源：[整负半权原返回](../notes/2026-11-27-unit211-equal-weight-negative-half-complete-original-return-8542.py)。

- 实际文件SHA256：5063af65da86c69b5d89dfd595e5a885f5b16443edd4683097e0d84f61c52e33。
- 本地Python3.12.14/python-flint0.9.0，单线程。
- 开始：2026-11-27 06:11:10.967835 UTC。
- 源数学完成0.205832464秒，驱动0.315394681秒，最大子进程RSS31272KiB，exit0。
- 源预算180秒/4GiB，驱动195秒。
- stdout26070字节，SHA256：63d526442a7b12058d6bee1b0a076c605ca3ab4f0358f9420cd00c129cb01cfa。
- [小回执](../notes/2026-11-27-unit211-equal-weight-negative-half-complete-execution-8542.json)。

所有旧分支的成功输入与准确失败身份保留在原附录；旧600秒QQ门仍冻结，没有作为总定理的额外复跑条件。后续直接转一般不等权及open中的原开放接口。
