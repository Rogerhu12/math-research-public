# R377：实际 q 全裂塔的准确阿贝尔化与两个非零 43 次幂关系

**状态：已证明。** 本文沿用 R171、R185、R243、R264、R327、R375 的同一个
$p=43$、776 bit 素数 $q$、$K=\mathbb Q(i)$、$F/K$、正算术 Artin 元
$\sigma$ 及全局普通元素
$$
 \Delta=\langle\sigma\rangle\simeq C_{44},\qquad
 \alpha=1+89460y,\qquad
 (\alpha)=\mathfrak q_0,\qquad N_{F/K}\alpha=-q.
 \tag{377.1}
$$
所有下标从零开始。R202 的规范 $\mathcal L$ 仍未求；本文的群是仅在 43
分歧、使全部 $q$ 素点全裂的塔，与原本在 $q$ 分歧的 $L/F$ 不同。

## 1. 结论

令 $F^{(43)}$ 为 $F$ 的最大仅在 43 分歧的 pro-43 扩张，令
$$
 \mathcal G=
 \operatorname{Gal}\bigl(F^{(43),\,q\text{-split}}/F\bigr).
$$
R327 已证明 $\operatorname{Gal}(F^{(43)}/F)$ 自由秩 45；R375 已实际算出
44 个 $q$ Frobenius 在其模 43 阿贝尔化中的秩为 41，并得
$d(\mathcal G)=4$、$r(\mathcal G)\le3$。

本次把同一批实际 Frobenius 提升到 $43^2$，得到准确的整结论
$$
 \boxed{\mathcal G^{\mathrm{ab}}
       \simeq \mathbb Z_{43}^{,2}\oplus
                    (\mathbb Z/43\mathbb Z)^2.}
 \tag{377.2}
$$
在 $\mathbb Z_{43}[\Delta]$ 模的意义下，自由部分的角色为 $0,22$，
有限部分是角色对 $16,28=-16\pmod{44}$：若 $\omega=8+25i\in\mathbb F_{43^2}$，
可写为
$$
 \mathcal G^{\mathrm{ab}}
 \simeq \mathbb Z_{43}(\mathbf1)\oplus\mathbb Z_{43}(\chi^{22})
          \oplus \mathbb F_{43^2}(\chi^{16}),
 \qquad \chi(\sigma)=\omega.
 \tag{377.3}
$$
末项视为二维 $\mathbb F_{43}$ 模；把 $16$ 换成 $28$ 给同构的有理表示。

因此
$$
                       2\le r(\mathcal G)\le3,
 \tag{377.4}
$$
且 $\mathcal G$ 不是自由 pro-43 群。可选取四元最小生成组及至多三个关系，
使三个关系的阿贝尔化为 $43e_1,43e_2,0$。这没有算出其交换子项，
也没有判定第三个关系是否冗余。

## 2. 同一个局部域与普通单位基

43 在 $F$ 中只有一个素点，完成域记为 $F_v$。沿 R185、R327 的实际
正规化取
$$
 C=70375455224064,\quad C\equiv38\pmod{43},\qquad
 \pi^{44}=C43,\qquad
 \sigma\pi=[\omega]^{-1}\pi.
 \tag{377.5}
$$
这里 $[\omega]$ 是 Teichmüller 提升，
$$
 [\omega]\equiv352+197i\pmod{43^2}.
 \tag{377.6}
$$
程序直接检查其阶为 44、十一阶幂为 $i$、二十二阶幂为 $-1$。
复共轭 $\tau$ 在该局部模型中固定 $\pi$，把 $i$ 变为 $-i$；
$\tau\sigma\tau=\sigma^{-1}$。

记 $\mathcal U=1+\mathfrak m_v$。局部域不含 $\mu_{43}$，因为
$43$ 次单位根的分歧指数 42 不整除 $e(F_v/\mathbb Q_{43})=44$。
故 $\mathcal U$ 是自由秩 88 的 $\mathbb Z_{43}$ 模。

把普通全局单位的局部 Teichmüller 因子除掉，并取闭包，记为 $\overline E$。
R327 已证明其在 $\mathcal U$ 中饱和，且下面 43 个实际单位给出
$\overline E$ 的 $\mathbb Z_{43}$ 基：
$$
 \eta=(\varepsilon_0,\ldots,\varepsilon_{21},
       \sigma\varepsilon_0,\ldots,\sigma\varepsilon_7,
       \sigma\varepsilon_9,\ldots,\sigma\varepsilon_{21}).
 \tag{377.7}
$$
$\varepsilon_j$ 正是 R243 的 22 个普通单位；它们各自的整多项式恒等式及
全局单位性已在 R243、R327 证明。此处仍用准确的全局 $z=h(y)/2$ 代入，
没有重新任取共轭或改变 $q$ 标签。

R264 的 $\mathrm{Cl}(F)[43^\infty]=0$ 与仅在 43 分歧的类域正合列给
$$
 G_{F,43}^{\mathrm{ab}}\simeq\mathcal U/\overline E
                               \simeq\mathbb Z_{43}^{45}.
 \tag{377.8}
$$
全局互反律的正算术方向仍为
$$
 \varphi_j=\operatorname{Frob}^{\mathrm{arith}}_{\mathfrak q_j}
       =-[\sigma^j\alpha]_v\pmod{\overline E},
 \qquad\mathfrak q_j=\sigma^j\mathfrak q_0.
 \tag{377.9}
$$
于是 $\mathcal G^{\mathrm{ab}}$ 是 (377.8) 除以这 44 个实际元素所生成的闭子模。

## 3. 一个完整的整 Artin–Hasse 基

定义
$$
 E_{43}(T)=\exp\left(\sum_{k\ge0}\frac{T^{43^k}}{43^k}\right).
$$
其系数在 $\mathbb Z_{43}$ 中：形式恒等式
$$
 E_{43}(T)=
 \prod_{\substack{n\ge1\\43\nmid n}}(1-T^n)^{-\mu(n)/n}
 \tag{377.10}
$$
由取形式对数逐项验证；每个指数属于 $\mathbb Z_{43}$，二项式展开整。
令
$$
 \mathcal R=\{1,2,\ldots,42,44,45\}.
$$
则下面 88 个单位给 $\mathcal U$ 的 $\mathbb Z_{43}$ 基：
$$
     E_{43}(\pi^r),\ E_{43}(i\pi^r),\qquad r\in\mathcal R.
 \tag{377.11}
$$

为完整说明基性，记 $U^n=1+\mathfrak m_v^n$。
因为 $2/44>1/(43-1)$，指数与对数在 $\mathfrak m_v^2$ 上互逆，故
$(U^2)^{43}=U^{46}$。而 $\mathcal U/U^2$ 有两个模 43 基元
$1+\pi,1+i\pi$；其 43 次幂在 $U^1/U^{46}$ 中是
$$
 1+\pi^{43}+43\pi,\qquad
 1-i\pi^{43}+43i\pi.
 \tag{377.12}
$$
所以 $\mathcal U/\mathcal U^{43}$ 维数为 $90-2=88$。
由于 $E_{43}(c\pi^r)=1+c\pi^r+O(\pi^{r+1})$，
若 (377.11) 的模 43 线性组合为 43 次幂，最小深度小于 43 的非零系数
不可能消失；先逐层迫 $r=1,\ldots,42$ 的系数全零。
剩下 $r=44,45$ 的组合若是 43 次幂，则 (377.12) 的深度 43 系数迫两个浅层
43 次幂的系数为零，它只能属于 $U^{46}$，从而深度 44、45 的系数也为零。
这证明模 43 独立，进而由 Nakayama 和无 43 挠性得到整基。

按每个 $r$ 的实、虚两个系数排列坐标。若一个坐标对为 $(a,b)$，
$\sigma^j$ 在它上面的作用就是乘以 $[\omega]^{-rj}$。
这在整 $\mathbb Z_{43}$ 上成立：
$$
 \log E_{43}(i\pi^r)
  =\sum_{k\ge0}\frac{(-1)^k i\pi^{r43^k}}{43^k},
$$
且 $[\omega]^{43}=\overline{[\omega]}$，故每个偶数、奇数项分别匹配实虚坐标。
因此只需求 22 个 $\varepsilon_j$ 和 $\alpha$ 的坐标，全部共轭由同一
$\sigma$ 的准确作用得到。

## 4. 有限环核验保证全部两位坐标真实

证书中的所有候选坐标均在实际有限环
$$
 \mathscr R=\mathcal O_{F_v}/(\pi^{90})
 \tag{377.13}
$$
内重新乘回核验。其标准表示是 44 个 Gaussian 系数：常数与 $\pi$ 系数
取模 $43^3$，其余 $\pi^2,\ldots,\pi^{43}$ 系数取模 $43^2$；
乘法只用 $\pi^{44}=C43$。这些混合模数正好表达 $\pi^{90}=0$。

若原 Eisenstein 多项式为
$$
 P_y(Y)=Y^{44}+43\sum_{j=0}^{43}c_jY^j,\qquad C=-c_0,
$$
则在 $\mathscr R$ 中直接 Newton 解
$$
 u^{44}-1+\sum_{j=1}^{43}(c_j/C)\pi^ju^j=0,\qquad u\equiv1\pmod\pi,
 \tag{377.14}
$$
并置 $y=\pi u$。七次迭代后程序检查方程和 $P_y(y)$ 都严格为零。
随后在此环内用原全局多项式计算 $z=h(y)/2$、22 个 $\varepsilon_j$ 和
$1+89460y$，而非用已存的对数值替代这些元素。

式 (377.11) 的有限环值也独立构造。写 $E_{43}(T)=\sum e_nT^n$，
在 $n<90$ 时用准确有理数递推
$$
 e_0=1,\qquad ne_n=e_{n-1}+e_{n-43},\qquad e_j=0\ (j<0).
 \tag{377.15}
$$
所有实际分母均检查与 43 互素。因 $\pi^{90}=0$，这些有限项给完整值。

所用的 43 平方幂判据也是准确的。由指数、对数
$(U^2)^{43^2}=U^{90}$，所以 $\mathcal U^{43^2}/U^{90}$ 恰由
$$
 \begin{aligned}
 G_1&=(1+\pi)^{43^2}
       =1+43\pi^{43}+43^2\pi,\\
 G_i&=(1+i\pi)^{43^2}
       =1-43i\pi^{43}+43^2i\pi
 \end{aligned}
 \quad\text{在 }\mathscr R\text{ 中}
 \tag{377.16}
$$
生成。这两个元素各有阶 43，深度 87 的实虚系数独立。

对每个实际元素 $g$，先除去其准确 Teichmüller 因子，再把证书的 44 个
实 Artin–Hasse 坐标 $b_r\in\mathbb Z/43^2$ 乘回。
程序逐一检查
$$
 \frac{g/[\bar g]}{\prod_{r\in\mathcal R}E_{43}(\pi^r)^{b_r}}
                        =G_1^aG_i^b\quad\text{在 }\mathscr R\text{ 中},
 \qquad 0\le a,b<43.
 \tag{377.17}
$$
全部 23 个等式通过；各自的 $(a,b)$ 与整个有限环商值均保存在证书。
式 (377.16) 证明 (377.17) 等价于所报坐标确为 $g$ 的模 $43^2$ 坐标。
因此该核验不依赖近似对数的尾项猜测。

候选坐标的快速生成也保存在同一脚本中：在
$(\mathbb Z/43^4)[[T]]/(T^{130})$ 解同一 $u$，
用 $43g'/g$ 积分，再按 $T^{44}=C43$ 整理为 (377.11)。
有限环 (377.17) 独立验证最终坐标；即使生成环节截断选错，也会被此等式检出。
同时检查所有普通单位的局部对数迹为零，以及
$44A_0(\alpha)=\log(-q)\pmod{43^3}$。

## 5. 实际矩阵与两个恰为一次的 43 因子

令 $U$ 是 (377.7) 在 (377.11) 下的 $88\times43$ 坐标矩阵，
令 $A$ 是再接上 $-\alpha_0,\ldots,-\alpha_{43}$ 的 $88\times87$ 矩阵。
全部矩阵均实际计算模 $43^2$。

先用 43 个模 43 非零枢轴把 $U$ 消成单位块，并将相同行变换作用在
Frobenius 列上。下方余下 $45\times44$ 矩阵 $Q$，即 (377.8) 中的
44 个实际 Frobenius。其模 43 枢轴正好为列 $0,\ldots,40$。
继续把这 41 列消为单位块，余下四行、三列均为 43 的倍数。
除以 43 后，实际矩阵为
$$
 D=\begin{pmatrix}
   23&7&27\\
   0&0&0\\
   0&0&0\\
   1&5&4
   \end{pmatrix}\quad\text{在 }\mathbb F_{43}\text{ 上}.
 \tag{377.18}
$$
这里三列按原 $q$ 标签依次为 $41,42,43$。子式
$$
 \det\begin{pmatrix}23&7\\1&5\end{pmatrix}
          =108\equiv22\not\equiv0\pmod{43}
 \tag{377.19}
$$
证明余下恰有两个 Smith 因子已在第一层 43 倍数处非零。
准确的整秩上界在下一节证明；不能仅凭模 $43^2$ 将第三方向宣布为整零。

角色也逐项验证。令
$$
 v_j^+=\Re([\omega]^{16j}),\qquad
 v_j^-=\Im([\omega]^{16j})\quad\pmod{43^2}.
$$
在本次确定的 45 行商基中，程序得到
$$
 Qv^+\equiv43\cdot29 e_{11},\qquad
 Qv^-\equiv43\cdot29 e_{12}\pmod{43^2},
 \tag{377.20}
$$
且其余各行均为零。这把 R375 模 43 的角色对 $\pm16$ 缺陷准确提升，
没有把它们当作永久的自由方向。交错向量 $((-1)^j)$ 的像模 $43^2$ 仍为零。

## 6. 二次角色上的整零关系

定义整幂等元
$$
                e_{22}=\frac1{44}\sum_{j=0}^{43}(-1)^j\sigma^j.
 \tag{377.21}
$$
因为 $44$ 在 $\mathbb Z_{43}$ 中可逆，此幂等元作用于整局部单位模。
在 (377.11) 中，$e_{22}\mathcal U$ 就是深度 $22$ 的实虚两个
$\mathbb Z_{43}$ 方向；其中 $\tau$ 固定部分 $W^+$ 为秩一。

R243、R264 的实际 Pell 单位
$$
       \epsilon=3482+531\sqrt{43},\qquad
       3482^2-43\cdot531^2=1
 \tag{377.22}
$$
在 $F$ 中，满足 $\tau\epsilon=\epsilon$、
$\sigma\epsilon=\epsilon^{-1}$，所以其局部主单位部分属于 $W^+$。
它非零：$\epsilon$ 不是根单位，而局部对数在 $\mathcal U$ 上单射。

因此 $W^+\cap\overline E$ 含秩一子模。由 R327 的整饱和性，
$\mathcal U/\overline E$ 无 43 挠性，故必有
$$
                              W^+\subseteq\overline E.
 \tag{377.23}
$$
具体地，对任意 $w\in W^+$，某个 $43^n w$ 落在由 $\epsilon$ 生成的
子模；若 $w$ 在商中非零，它便产生 43 幂挠性，矛盾。

$\alpha$ 被 $\tau$ 固定，而 $\tau e_{22}\tau=e_{22}$，所以
$e_{22}[\alpha]_v\in W^+$。结合 (377.9)、(377.23)，得到准确的整关系
$$
                 \boxed{\sum_{j=0}^{43}(-1)^j\varphi_j=0
                         \quad\text{在 }G_{F,43}^{\mathrm{ab}}.}
 \tag{377.24}
$$
这是 $\mathbb Z_{43}^{44}\to G_{F,43}^{\mathrm{ab}}$ 核中的一个本原向量。
故该映射整秩至多 43。

## 7. Smith 因子、角色及关系数

模 43 秩 41 给出 41 个单位 Smith 因子；式 (377.18)–(377.19)
给出两个恰一次的 43 因子。这个判断只需模 $43^2$：先消去单位块，
残块为 $43D+43^2B$，而 $D$ 有秩二，故其中两个不变因子赋值准确为一。
式 (377.24) 又把总秩限制在 43，因此没有第四十四个更深的非零因子。
于是所有非零 Smith 因子的赋值准确为
$$
                   \underbrace{0,\ldots,0}_{41},1,1,
 \tag{377.25}
$$
而 $45$ 维的目标商留下自由秩二，证明 (377.2)。

角色说明可同时从结构和实际矩阵看出。Dirichlet 对数在有理数上把
$F$ 的全局单位表示识别为 $\Delta$ 的正则表示去掉平凡表示，
因为 44 个复无穷位由 $\Delta$ 正则置换。故每个非平凡角色的全局单位秩为一。
二次角色中的实方向由 (377.23) 全部消去，虚方向留下；平凡角色中没有
全局单位方向，实际 $\alpha$ 的深度 44 坐标为 $931\equiv28\pmod{43}$，
它原始地消去实方向，虚方向留下。R375 的其他角色均已模 43 满秩，
因此在整 $\mathbb Z_{43}$ 上无剩余商。
唯一有限部分由 (377.20) 标定为 $\chi^{16}\oplus\chi^{28}$。
由于 $43\nmid44$，这些不同角色块整分裂，得到 (377.3)。

R375 给一个四生成、至多三关系的 pro-43 表示；任何四元最小表示的关系
阿贝尔化都必须生成秩二子模，所以关系数至少二。对自由生成元及关系作
可逆 $\mathbb Z_{43}$ 基变换，可把其阿贝尔化矩阵变为
$\operatorname{diag}(43,43,0)$，给出 (377.4) 后的描述。
此类基变换可提升为自由 pro-43 群的基变换：初等行操作对应生成元相乘，
单位对角元对应取 $\mathbb Z_{43}^{\times}$ 次幂，所得模 43 生成组仍为基。
对关系生成组同理；零列仅表示交换子部分未定，不表示关系恒等。

## 8. 复算入口与准确边界

正式产物：

- `scripts/verify_r377_q_frobenius_smith.py`；
- `notes/r377_q_frobenius_smith_certificate.json`；
- 本证明。

复算命令为

```bash
python scripts/verify_r377_q_frobenius_smith.py notes \
  --certificate notes/r377_q_frobenius_smith_certificate.json --progress
```

验证器仅使用 Python 标准库。它从 R171、R185、R243 的原始证书重建全部
23 个普通元素、全部模 $43^2$ Artin–Hasse 坐标、$88\times87$ 矩阵、
$45\times44$ 商矩阵、剩余矩阵 (377.18) 及角色像 (377.20)，并在实际
有限环中逐个重放 (377.17)。输入 SHA256、所有矩阵和 23 个有限环商值
均保存在证书。

本次没有使用 GRH。全局单位饱和性、基域类群消失和自由性分别使用已有
R327、R264 的完整结论；二次角色上的整零关系由第 6 节单独证明，
没有从有限精度零值推断。

**仍未完成的量。** 本文没有求三个非阿贝尔 $q$ Frobenius 关系字的交换子项，
没有判断第三关系冗余，也没有求 R311 固定普通上层单位 $X/Y$ 的坐标或
其 R322 唯一 $q$ 相位。原本在 $q$ 分歧的 $L/F$ 不属于这里的 $q$ 全裂塔。
所以 (377.2) 不给 R202 的规范 $\mathcal L$、$\rho=\mathcal L+3$，
也不替代非单位范数见证中必须保留的外支撑正 Artin 修正。

## 依赖定位

- R171：同一 $\alpha$、$q$、$N_{F/K}\alpha=-q$ 及主素点标签。
- R185、R327：同一局部 $\pi$、$\sigma\pi=[\omega]^{-1}\pi$ 与全局 $z=h(y)/2$。
- R243：22 个实际普通单位及 Pell 单位 (377.22)。
- R264：完整 $\mathrm{Cl}(F)[43^\infty]=0$。
- R327：实际普通单位局部模 43 单射、整饱和、仅 43 分歧群自由秩 45。
- R375：正算术 Frobenius 方向、秩 41、角色 $\pm16,22$、四生成三关系上界。

仅在 43 分歧的类域正合列及 p-rational 自由性判据的原刊定位见 R327；
本文的 Artin–Hasse 基性、有限精度认证、整零关系和 Smith 推论均已在正文证明。
