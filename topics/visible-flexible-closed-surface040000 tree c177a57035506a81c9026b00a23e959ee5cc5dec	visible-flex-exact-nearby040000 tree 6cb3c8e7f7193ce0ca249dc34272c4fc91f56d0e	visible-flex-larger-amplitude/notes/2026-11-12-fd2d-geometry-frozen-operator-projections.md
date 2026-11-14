# 冻结角投影缓存：原算式、视图绑定与实际两点对照

2026-11-12，fd2d geometry。服务新的低内存求解进程，不修改正在运行的 23、原 provider 源或任何已保存数学场。

## 1. 哪四个矩阵确实与物理参数无关

原 `fd2d_gc_raw_bump_dae.py::RawBumpDAE.operators(delta)` 在每个实际径向位置 $s$ 上使用冻结角图

$$
\omega=U_\xi,\qquad v=U_s/U_\xi.
$$

角基与投影矩阵记作 $E,O,E_\xi,O_\xi,P_E,P_O$。原 operator 的四个矩阵乘积中，可以冻结

$$
A=P_E\operatorname{diag}(v)E_\xi,\qquad
B=P_E\operatorname{diag}(1/\omega)O_\xi,
$$

$$
C=P_O\operatorname{diag}(v)O_\xi,\qquad
D=P_O\operatorname{diag}(1/\omega)E_\xi.
\tag{1}
$$

令 $e=K+1$。按原 correction 的 $n,m,l$ 列分组，原矩阵准确等于

$$
\mathcal O_\delta(s)=
\begin{pmatrix}
A-c_\delta I_e & B/a_\delta & c_\delta I_e\\
0 & C-2c_\delta I_K & D/a_\delta
\end{pmatrix}.
\tag{2}
$$

证明只有矩阵投影的线性：在一个固定径向位置，$a_\delta$ 不依赖角度，故其倒数可以移出角向矩阵乘积。原 $v,\omega$、角基及投影都不随当前 $\delta$ 或尾/中央控制变化。

所以新共享缓存只存 (1)。每次缺少原局部参数 packet 时仍由原 profile provider 计算实际 $a_\delta,c_\delta,K_\delta$ 及其参数 jets。原输出 `inv` 仍用原来的 `1/(U_xi*a)` 求值，forcing、完整场、残差以及参数依赖 lifting 均不进入新共享缓存。

原代码已有的最多 4 个局部 `delta.tobytes()` operator packets 保留原作用域。相同坐标的 affine/background clone 可以如原 `__dict__.update` 逻辑共享这些旧 packet；它们没有被提升为跨不同坐标的共享冻结缓存。新薄层另核实际坐标上下文，在一个 view 的坐标变动时清空其旧局部 packet。

## 2. 实数相同与浮点重分配

实数算术中的 (2) 与原算式完全相同，未更改方程、未知量、物理 $g$ 或有限角投影。实际 binary64 中，原来的

```python
PE @ ((1/(U_xi*a))[:,None] * Ox)
```

改为

```python
(PE @ ((1/U_xi)[:,None] * Ox)) / a
```

因此不承诺逐字节相同。另一块 $P_O/E_\xi$ 同理；其余两个 advection 投影的算式不变。

对物理参数方向，有 $\dot A=\dot B=\dot C=\dot D=0$，故

$$
\dot{\mathcal O}=
\begin{pmatrix}
-\dot c I_e & -B\dot a/a^2 & \dot c I_e\\
0 & -2\dot c I_K & -D\dot a/a^2
\end{pmatrix}.
\tag{3}
$$

辅助函数只为局部算式核查提供 (3)；没有替换现有 solver 的完整 Jacobian 链式项。原 profile jets 及全部 $\delta$ 导数仍由原 provider 负责。

## 3. 确切键、有界共享和 copy 视图

实现是另名文件

`scripts/fd2d_gc_frozen_operator_projections.py`，SHA256
`a91804d7bb70d35cef018c73213d61cca7918df0f3621b8c4bbbda5dd73a2798`。

一个共享对象只绑定同一个数学 chart 对象、完整 atlas 定义、实际 Fourier 布局、固定计算角列，以及 $P_E,P_O,E_\xi,O_\xi$ 的 dtype、shape 和完整 binary64 字节。调用时重新核这些定义，不只按 $K$ 或节点数判断。

每个点的 LRU 键使用实际 binary64 $s$ 以及该点完整 `u,u_s,u_xi,advection` 角列的原始字节。字节 tuple 本身参与相等判断；报告中的 SHA 是复现身份，不替代实际列内容匹配。坐标只差一个浮点位也不会误命中。

默认上限为 32 MiB 的**计数 payload**和 1024 个点。计数包含冻结 basis/key 字节和已缓存矩阵的 ndarray payload；它不声称限制 Python 解释器开销、现存局部参数 packet、view 自身或全部进程 RSS。超额按 LRU 淘汰；单项超过可用 payload 时只求值、不插入。缓存中的四个矩阵设为只读，不改变原 problem 的 basis 数组。

安装使用只作用于该新对象的动态 thin mixin，不在实例中保存绑定到父对象的 `MethodType`。因此 `copy.copy` 得到的径向/求积 view，其 `operators(self,delta)` 中的 `self` 仍是该 view，自身的 $N,x,coords$ 不会错误回指全 problem。

还处理了原 R155 的显式基类构造：`coast_background_view()` 先完整执行原 `PositiveGaussRawBumpDAE.__new__` 与原字段/残差计数逻辑，再只给所得背景 view 附上同一薄层。随后 R153 的 `affine_view()` 也保留它。没有进程全局的基类 patch，也没有修改闭 source。已有派生 view 的纯运行缓存在安装时丢弃，定义数组与数学 packet 不变。

## 4. 实际唯一小核

输入为当前不可变 22 accepted1：

`notes/2026-11-12-fd2d-raw-bump-lowmem22-b0001-accepted-0001.npz`，SHA256
`4251d15d3c78675ba8bbaf6cc2b71eb82bf78b8b6138e481aead56d73b6a0f68`。

以 R163 v3 的空细分恢复该实际 K31/tail16、129 节点场。只取输入节点 64、65：

$$
s=(0.6116816746501718,\ 0.6313633493003443).
$$

使用该态真实非零 $\delta$，以及一个明示小的非零 $\delta$ 变化；旧新都在这两个相同点上计算。另以一个明示方向比较 (3) 与原未提取 $1/a$ 的投影导数，并比较混合状态/参数 RHS JVP。

真实 session `93032`，初始 chunk `9bbca9`，最终 chunk `bc2db1`，自然 exit0；用时 6.247511153 秒，峰值 RSS 92760 KiB。源为 `scripts/fd2d-frozen-operator-projections-check.py`；报告为

`notes/2026-11-12-fd2d-frozen-operator-projections-check-01.json`，SHA256
`d244191456f5125de697591c7b4cd7e1fd6839c215245b1c7532c955e5d0a2d1`。

| 局部比较 | 真实最大 scaled 差 |
| --- | ---: |
| 两个非零 $\delta$ 的 operator | $5.431\times10^{-15}$ |
| operator 的参数 JVP | $2.377\times10^{-15}$ |
| 两点实际 R153/R155 局部残差 | $9.735\times10^{-14}$ |

scaled 差定义为 $|new-old|/(1+|old|)$。本次两个点上，**全部 scalar/profile parameter jets、完整字段、Gauss、lifting forcing 均逐字节相同**。局部 Codazzi/残差的最大绝对差为 $1.457\times10^{-13}$，与投影中 $1/a$ 的浮点重分配一致。这里是有限双精度兼容核查，不是连续误差证书。

第一次两点调用真实 miss 数为 2；换非零 $\delta$ 后 miss 仍为 2、hit 增为 2，说明共享对象没有把参数变化错误视为新的角图。另一个仅含第二点的新 `radial_view` 返回形状 $(1,63,95)$，与原两点矩阵的相应切片逐字节相同，方法确实绑定到该单点 view。

实际旧新两点 `evaluate(...,jacobian=False)` 链都被调用一次。新链的显式 coast-background 和 affine view 均共享同一缓存，实际 wrap 计数为 2；不是只检查外层直接调用而遗漏 R155 内层路径。原完整数学定义 packet 全部保持原字节语义。

最终共享缓存有 2 个点，计数 payload 为 616480 B，固定 basis/key 部分 520192 B；5 次点命中、2 次点 miss。两点初次 miss 调用约 .001068 秒，换 $\delta$ 后的命中调用约 .000447 秒。它们只描述本小核，不能当完整 solver 的速度测量，也不证明此前退出 $-9$ 的原因或已被修复。

本次没有全域 objective、whole Jacobian、body、非线性 BVP 或活动进程修改。

## 5. 直接消费接口

在一个新 problem 由 R163 v3 恢复实际保存 mesh 后、首次 objective 和派生 view 前调用：

```python
from fd2d_gc_frozen_operator_projections import (
    install_frozen_operator_projection_cache,
)

handle = install_frozen_operator_projection_cache(
    problem, byte_limit=32*1024*1024, maximum_entries=1024,
)
runtime_definition = handle.binding
runtime_binding_sha256 = handle.binding_sha256
runtime_statistics = handle.statistics()
```

`handle.binding` 是 JSON 可序列化定义 dict，而不是方法。不要把运行 hit/miss 计数写进数学场身份；新 driver 的独立 runtime provenance 可记录这些信息。

此薄层只读 `problem.coords`，不改 chart/reference 实例方法，可与 metric 的独立 `install_prepared_geometry_cache` 同装。当前两个层的单独小核均已完成；本稿没有追加整轮联合求解，也不将额外联合测试设为新 gate。
