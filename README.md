package cuoi_ky_nhom_26;

import java.lang.Iterable;
public interface QueueInterface<E> extends Iterable<E> {
    public void enqueue(E element);
    public E dequeue();
    public boolean isEmpty();
    public int size();
    public void show();
}
