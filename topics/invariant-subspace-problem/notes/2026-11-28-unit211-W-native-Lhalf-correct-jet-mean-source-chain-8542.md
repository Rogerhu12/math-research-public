# W 原 native / Lhalf 来源链：mean(1) 的静态定义核对

日期：2026-11-28 UTC。会话：Astra-ISP-8542378f-20261127。
这是对冻结源的文字与 SHA 核对，没有重新运行任何数学门。

## 1. 发现的定义差异

另一个 compact JS 路径把 jet 分量 $j=1$ 的平方项写成
$-2d_1^2$。原四维代数的乘法是

$$
(vw)_1=v_0w_1+v_1w_0,
$$

所以正确的这一项是

$$
-2(d^2)_1=-4d_0d_1.
$$

两定义的差为 $4d_0d_1-2d_1^2$。
其它路径是否承继错误，需要逐源检查；本说明只对下面完整明确的 W 链作结论。

## 2. W 的原源直接使用正确 jet 乘法

冻结 raw C9 源
`2026-11-27-unit211-generic-LS-W-C9-six-generator-original-parameter-cofactors-8542.py`
的 SHA256 为
`10720660772a9a1252b905b1227b697e038d1b974b7e96ec30e485477b21d3f1`，
blob 为 `a1a9d02a1602a47398ba9bbb9295b3da7d7ddd37`。

它自含原 Gram 与迹，没有 compact JS 依赖。原文是：

~~~python
def vm(v,z):
 return [v[0]*z[0],v[0]*z[1]+v[1]*z[0],v[2]*z[2],v[3]*z[3]]
def mean(j):
 ee=2*tau(vm(rows[0],rows[1])) if j==1 else tau(vm(rows[j],rows[j]))
 return ee-2*Kd[j]-2*vm(d,d)[j]+2*F2*d[j]
assert not mean(0)
E1,EB,EC=mean(1),mean(2),mean(3)
~~~

随后原系统直接取
`symbolic['E1']=E1.a`、
`EBe=EB.a`、`EBo=EB.b`。
原 N4/P2 也使用同一个 `vm`。
故 $j=1$ 项准确为 $-4d_0d_1$。

## 3. 新整 Lhalf 证明的全部构造依赖

依赖只有以下单向链，不从有缺口的 compact JS 取任何必要式：

| 源 | SHA256 | 入口 |
|---|---|---|
| raw C9 | `10720660772a9a1252b905b1227b697e038d1b974b7e96ec30e485477b21d3f1` | 自含正确原 Gram |
| native 六行 | `eca419501bf348518fe4f36582d417784235cc7c35872f1a1eb180c88b1e537d` | raw C9 的固定必要前缀 |
| 整 Lhalf 的 G D 返回 | `53c744cfb54beccaae092fb51ab9869331a0b801361eefc5e2e0032d674bdf0f` | native 的 8074 字节必要前缀 |
| F101 全有限返回 | `d5be6f7eaa25eb1520ab6cb549938d86886b78ba82a43fead922c41552694f0d` | 上一源的 14141 字节参数定义前缀 |

native 的六行、三轴矩阵以及第七条 commutator 行都对这一正确原系统实际返回。
G D 身份直接核同一个原 D 六坐标；F101 的全部有限模型使用同一原行与 D 目标。
最终全 Lhalf 排除不依赖错误 compact 式，也不以旧 I11 的泛型维数作为其运行结论的必要前提。

native 中所用 C9、J19、旧 H 及等权等已付整支仍按其各自正式原来源引用；
它们不被这个静态核对重新证明。此处没有新增或改写任何支付条件。

## 4. 引发本次核对的直接原 Gram 检查

取 $\ell=a=1/2$、$\gamma^2=0$，原 Gram 行为

$$
(0,0,p,q),\quad(0,0,\gamma,\gamma),\quad
(p,\gamma,0,0),\quad(q,\gamma,0,0).
$$

原定义给

$$
d=(u,\gamma/2,p/2+\gamma,q/2+\gamma),\qquad F_2=u+\gamma.
$$

正确 mean(1) 的四项依次为
$2u\gamma,-u\gamma,-2u\gamma,+u\gamma$，总和为零。
B 行四项依次为

$$
\frac{p^2}{2}+2p\gamma,\quad
-up-p\gamma-2u\gamma,\quad
-\frac{p^2}{2}-2p\gamma,\quad
up+2u\gamma+p\gamma,
$$

也为零。这个直接原输入说明了为何不能把 compact 的不同平方定义带回 W。
正式已刊 W 双数族继续保持其准确 W 范围，本说明不借此扩张其它分支的结论。

本次不改任何已执行源字节、不猜运行状态、不重放已成门。
